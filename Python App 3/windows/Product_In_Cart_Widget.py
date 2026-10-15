from ui.Ui_product_in_cart_widget import Ui_Form
from PySide6.QtWidgets import QWidget,QMessageBox
from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from db import db

class ProductInCartWidget(Ui_Form,QWidget):
    def __init__(self,product, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_StyledBackground,True)

        self.parent = parent
        self.product = product
        self.load_data()
        self.delete_btn.clicked.connect(self.delete)

    def load_data(self):
        self.name.setText(f"{self.product['name']} | {self.product['manufacture']}")
        self.cat.setText(self.product['category'])
        self.structure.setText(f"Выбранный размер: {self.product['selected_size']}")
        self.total_count.setText(f"Кол-во: {self.product['selected_count']}")
        self.price.setText(f"Цена: {self.product['price'] * self.product['selected_count']}")
        self.img.setPixmap(QPixmap(f"img/{self.product['img']}"))


    def delete(self):
        for p in db.all_products:
            for stock in p['stocks']:
                if stock['id_stock'] == self.product['selected_stock']:
                    stock['count'] += self.product['selected_count']
                    p['total_count'] += self.product['selected_count']

                    if p['total_count'] > 0:
                        p['hidden'] = False
        db.cart.remove(self.product)
        total_price = 0
        for c in db.cart:
            total_price += c['selected_count'] * c['price']
        self.parent.parent.filter_products()
        self.parent.total_price.setText(f"Сумма: {total_price}")
        
        self.deleteLater()
