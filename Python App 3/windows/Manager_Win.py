from ui.Ui_manager_win import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QMessageBox
from db import db

class ManagerWindow(Ui_MainWindow,QMainWindow):
    def __init__(self,user, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.is_guest = False
        self.cart_btn.clicked.connect(self.open_cart)
        self.user = user
        self.user_data.setText(f"{user.surname} {user.name} {user.lastname}")
        self.load_boxes()
        self.filter_products()
        self.cat_box.currentIndexChanged.connect(self.filter_products)
        self.scat_box.currentIndexChanged.connect(self.filter_products)
        self.price_box.currentIndexChanged.connect(self.filter_products)
        self.search_edit.textChanged.connect(self.filter_products)
        self.logout_btn.clicked.connect(self.logout)

        self.orders_btn.clicked.connect(self.open_orders)
        

    def load_boxes(self):
        self.cat_box.addItem('Все',0)
        self.scat_box.addItem('Все',0)
        self.price_box.addItem('Все',0)
        self.price_box.addItem('Дешевле',1)
        self.price_box.addItem('Дороже',2)

        for cat in db.get_categories():
            self.cat_box.addItem(cat['name'],cat['id'])
        for scat in db.get_subcategories():
            self.scat_box.addItem(scat['name'],scat['id'])

    def load_widgets(self,products = None):
        if products == None:
            products = db.all_products
        from windows.Product_Widget import ProductWidget
        layout = self.scrollAreaWidgetContents.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for p in products:
            if not p['hidden']:
                layout.addWidget(ProductWidget(p,self))

    def filter_products(self):
        price = self.price_box.currentText()
        cat = self.cat_box.currentText()
        scat = self.scat_box.currentText()
        search = self.search_edit.text().lower()

        result = db.all_products

        if cat != 'Все':
            result = [p for p in result if p['category'] == cat]
        if scat != 'Все':
            result = [p for p in result if p['subcategory'] == scat]
        if search != 'Все':
            result = [p for p in result if search in p['name'].lower()]

        if price !='Все':
            if price !='Дороже':
                result.sort(key=lambda x: x['price'])
            else:
                result.sort(key=lambda x: x['price'], reverse=True)
        self.load_widgets(result)

    def logout(self):
        from windows.Auth_Win import AuthWindow
        self.win = AuthWindow()
        self.win.show()
        self.close()

    def open_cart(self):
        from windows.Cart_Win import CartWindow
        self.win = CartWindow(self)
        self.win.show()

    def open_orders(self):
        from windows.Orders_Win import OrdersWindow
        self.win = OrdersWindow(self)
        self.win.show()