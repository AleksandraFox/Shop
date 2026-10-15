from datetime import date
from PySide6.QtWidgets import QMessageBox
from sqlalchemy import extract, select
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base


class Database:
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:12345@localhost/Practica')
        self.session = Session(self.engine)
        base = automap_base()
        base.prepare(self.engine)

        self.STOCKS_FIELDS = {'count','id_stock','size'}
        self.ORDERS_FIELDS = {'id_order_item','id_stock','size_name','product_name','count','price','product_id','product_img','product_description','product_structure','product_price','product_category','product_subcategory','product_manufacture'}

        self.users = base.classes.users
        self.stocks = base.classes.stocks
        self.orders = base.classes.orders
        self.order_items = base.classes.order_items
        self.manufactures = base.classes.manufactures
        self.categories = base.classes.categories
        self.subcategories = base.classes.subcategories
        self.products = base.classes.products
        self.sizes = base.classes.sizes

        self.all_products = self.group_products()
        self.cart = []

    def get_categories(self):
        stmt = (
            select(self.categories.id,self.categories.name)
        )
        result = self.session.execute(stmt).all()
        return [dict(row._mapping) for row in result]
    
    def get_subcategories(self):
        stmt = (
            select(self.subcategories.id,self.subcategories.name)
        )
        result = self.session.execute(stmt).all()
        return [dict(row._mapping) for row in result]

    def get_user(self,login_val):
        stmt = (
            select(self.users)
            .where(self.users.login == login_val)
        )
        result = self.session.execute(stmt).first()
        return [] if not result else result[0]

    def get_products(self):
        stmt = (
            select(
                self.products.id.label('id_product'),
                self.categories.name.label('category'),
                self.subcategories.name.label('subcategory'),
                self.products.img,
                self.products.name,
                self.manufactures.name.label('manufacture'),
                self.products.description,
                self.products.structure,
                self.products.price,

                self.stocks.id.label('id_stock'),
                self.sizes.name.label('size'),
                self.stocks.count
            )
            .join(self.stocks,self.stocks.id_product == self.products.id)
            .join(self.sizes,self.stocks.id_size == self.sizes.id)
            .join(self.manufactures,self.manufactures.id == self.products.id_manufacture)
            .join(self.categories,self.categories.id == self.products.id_category)
            .join(self.subcategories,self.subcategories.id == self.products.id_subcategory)
        )

        result = self.session.execute(stmt).all()
        return [dict(row._mapping) for row in result]

    def group_products(self):
        group = {}

        for p in self.get_products():
            id_product = p['id_product']

            if id_product not in group:
                group[id_product] = {
                    **p,
                    'total_count':0,
                    'stocks':[],
                    'hidden':False
                }

            item = group[id_product]
            item['total_count'] += p['count']
            item['stocks'].append({
                'id_stock':p['id_stock'],
                'size':p['size'],
                'count':p['count']
            })
            for key in self.STOCKS_FIELDS:
                group.pop(key,None)
        return list(group.values())

    def create_order(self,id_user):
        if len(self.cart):
            try:
                order = self.orders(
                    date = date.today(),
                    id_user = id_user
                )
                self.session.add(order)
                self.session.flush()

                for c in self.cart:
                    stock = self.session.get(self.stocks,c['selected_stock'])
                    if not stock:
                        raise ValueError('Нет сток')
                    if stock.count < c['selected_count']:
                        raise ValueError('В стоке товара меньше')
                    stock.count -= c['selected_count']

                    order_item = self.order_items(
                        id_order = order.id,
                        id_stock = c['selected_stock'],
                        count = c['selected_count'],
                        price = c['price']
                    )
                    self.session.add(order_item)
                self.session.commit()
                QMessageBox.information(None,'Успех','Заказ создан!')
                self.cart.clear()


            except Exception as e:
                self.session.rollback()
                QMessageBox.warning(None,'Ошибка',str(e))

    def get_orders(self):
        stmt = (
            select(
                self.orders.id.label('id_order'),
                self.users.id.label('id_user'),
                self.users.surname.label('user_surname'),
                self.users.name.label('user_name'),
                self.orders.date,

                self.order_items.id.label('id_order_item'),
                self.order_items.count,
                self.order_items.price,

                self.products.id.label('product_id'),
                self.products.name.label('product_name'),
                self.products.img.label('product_img'),
                self.products.description.label('product_description'),
                self.products.structure.label('product_structure'),
                self.products.price.label('product_price'),
                self.categories.name.label('product_category'),
                self.subcategories.name.label('product_subcategory'),
                self.manufactures.name.label('product_manufacture'),

                self.sizes.name.label('size_name'),
                self.stocks.id.label('id_stock')
            )
            .join(self.order_items,self.orders.id == self.order_items.id_order)
            .join(self.stocks, self.order_items.id_stock == self.stocks.id)
            .join(self.users,self.users.id == self.orders.id_user)
            .join(self.sizes, self.stocks.id_size == self.sizes.id)
            .join(self.products, self.products.id == self.stocks.id_product)
            .join(self.categories,self.categories.id == self.products.id_category)
            .join(self.subcategories,self.subcategories.id == self.products.id_subcategory)
            .join(self.manufactures,self.manufactures.id == self.products.id_manufacture)
        )
        result = self.session.execute(stmt).all()
        return [dict(row._mapping) for row in result]

    def group_orders(self):
        group = {}
    
        for o in self.get_orders():
            id_order = o['id_order']

            if id_order not in group:
                group[id_order] = {
                    **o,
                    'total_count':0,
                    'order_items':[],
                    'total_price':0
                }
            item = group[id_order]
            item['total_count'] += o['count']
            item['total_price'] += o['price']
            item['order_items'].append({
                'order_item':o['id_order_item'],
                'stock':o['id_stock'],
                'size':o['size_name'],
                'product':{
                            'id':o['product_id'],
                            'category':o['product_category'],
                            'subcategory':o['product_subcategory'],
                            'img':o['product_img'],
                            'name':o['product_name'],
                            'manufacture':o['product_manufacture'],
                            'description':o['product_description'],
                            'structure':o['product_structure'],
                            'price':o['product_price']
                                },
                'count':o['count'],
                'price':o['price']
            })
            for key in self.ORDERS_FIELDS:
                group.pop(key,None)
        return list(group.values())

    def change_order(self):
        pass

    def delete_order(self,order):
        try:
            for oi in order['order_items']:
                stock = self.session.get(self.stocks,oi['stock'])
                if stock:
                    stock.count += oi['count']
                    order_item = self.session.get(self.order_items,oi['order_item'])
                    self.session.delete(order_item)
                else:
                    raise ValueError('Нет стока!')
            o = self.session.get(self.orders,order['id_order'])
            if o:
                self.session.delete(o)
            else:
                raise ValueError('Нет заказа!')

            self.session.commit()
            QMessageBox.information(None,'Успех','Заказ и его позиции удалены!')
        except Exception as e:
            self.session.rollback()
            QMessageBox.warning(None,'Ошибка!',str(e))

    def create_order_manager(self,data):
        try:
            order = self.orders(
                date = date.today(),
                id_user = data['id_user']
            )
            self.session.add(order)
            self.session.flush()

            for item in data['stocks']:
                stock = self.session.execute(
                    select(
                        self.stocks
                    )
                    .where(self.stocks.id_size == item['id_size'])
                    .where(self.stocks.id_product == item['id_product'])
                ).scalar_one_or_none()
            
                if stock:
                    if stock.count >= item['count']:
                        stock.count -= item['count']
                        order_item = self.order_items(
                            id_order = order.id,
                            id_stock = stock.id,
                            count = item['count'],
                            price = item['price']
                        )
                        self.session.add(order_item)
                    else:
                        raise ValueError('Не хватает товаров!')
                else:
                    raise ValueError('Нет стока!')
            self.session.commit()
            QMessageBox.information(None,'Успех','Заказ добавлен!')
                            
        except Exception as e:
            self.session.rollback()
            QMessageBox.warning(None,'Ошибка',str(e))

db = Database()