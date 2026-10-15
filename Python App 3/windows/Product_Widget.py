from ui.Ui_product_widget import Ui_Form
from PySide6.QtWidgets import QWidget,QMessageBox
from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from db import db

class ProductWidget(Ui_Form,QWidget):
    def __init__(self,product, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_StyledBackground,True)
        self.parent = parent
        self.product = product
        self.load_data()
        self.mousePressEvent = self.on_click


    def load_data(self):
        self.name.setText(f"{self.product['name']} | {self.product['manufacture']}")
        self.cat.setText(self.product['category'])
        self.structure.setText(self.product['structure'])
        self.total_count.setText(f"Кол-во: {self.product['total_count']}")
        self.price.setText(f"Цена: {self.product['price']}")
        self.img.setPixmap(QPixmap(f"img/{self.product['img']}"))

        if self.product['total_count'] <= 3:
            self.setStyleSheet(self.styleSheet() + "#Form{"
            "border-color:#FF8080;}")


    def on_click(self,event):
        if event.buttons() == QtCore.Qt.LeftButton and not self.parent.is_guest:
            from windows.Product_Win import ProductWindow
            self.win = ProductWindow(self.product,self)
            self.win.show()
