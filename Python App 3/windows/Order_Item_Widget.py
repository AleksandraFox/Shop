from ui.Ui_order_item_widget import Ui_Form
from PySide6.QtWidgets import QWidget,QMessageBox
from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from db import db

class OrderItemWidget(Ui_Form,QWidget):
    def __init__(self,order_item, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_StyledBackground,True)
        self.parent = parent
        self.order_item = order_item
        self.load_data()


    def load_data(self):
        self.name.setText(f"{self.order_item['product']['name']} | {self.order_item['product']['manufacture']}")
        self.cat.setText(self.order_item['product']['category'])
        self.structure.setText(f"Выбранный размер: {self.order_item['size']}")
        self.total_count.setText(f"Кол-во: {self.order_item['count']}")
        self.price.setText(f"Цена: {self.order_item['product']['price']} * {self.order_item['count']} = {self.order_item['product']['price']*self.order_item['count']}")
        self.img.setPixmap(QPixmap(f"img/{self.order_item['product']['img']}"))
