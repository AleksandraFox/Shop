from ui.Ui_product_win import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QMessageBox
from db import db
from PySide6.QtGui import QPixmap

class ProductWindow(Ui_MainWindow,QMainWindow):
    def __init__(self,product, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.product = product
        self.load_data()
        self.load_sizes()
        self.set_maximum()
        self.cancel_btn.clicked.connect(lambda:self.close())
        self.size_box.currentIndexChanged.connect(self.set_maximum)
        self.to_cart_btn.clicked.connect(self.to_cart)

    def load_data(self):
        self.name.setText(self.product['name'])
        self.manufacture.setText(self.product['manufacture'])
        self.cat.setText(self.product['category'])
        self.scat.setText(self.product['subcategory'])
        self.structure.setText(self.product['structure'])
        self.total_count.setText(f"Кол-во: {self.product['total_count']}")
        self.price.setText(f"Цена: {self.product['price']}")
        self.img.setPixmap(QPixmap(f"img/{self.product['img']}"))

    def load_sizes(self):
        for stock in self.product['stocks']:
            if stock['count'] > 0:
                self.size_box.addItem(stock['size'],stock['id_stock'])

    def set_maximum(self):
        for stock in self.product['stocks']:
            if stock['size'] == self.size_box.currentText():
                self.count_spin.setMaximum(stock['count'])

    def to_cart(self):
        for p in db.all_products:
            for stock in p['stocks']:
                if stock['id_stock'] == self.size_box.currentData():
                    stock['count'] -= self.count_spin.value()
                    p['total_count'] -= self.count_spin.value()
                    if p['total_count'] < 1:
                        p['hidden'] = True

        db.cart.append({
            **self.product,
            'selected_count':self.count_spin.value(),
            'selected_stock':self.size_box.currentData(),
            'selected_size':self.size_box.currentText()
        })
        self.parent.window().filter_products()
        self.close()
