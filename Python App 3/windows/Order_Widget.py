from ui.Ui_order_widget import Ui_Form
from PySide6.QtWidgets import QWidget,QMessageBox
from PySide6 import QtCore
from PySide6.QtGui import QPixmap
from db import db

class OrderWidget(Ui_Form,QWidget):
    def __init__(self,order, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_StyledBackground,True)
        self.parent = parent
        self.order = order
        self.load_data()
        self.mousePressEvent = self.on_click
        self.delete_order_btn.clicked.connect(self.remove_order)


    def load_data(self):
        self.id_order.setText(f"Номер: {self.order['id_order']}")
        self.date.setText(f"Дата: {self.order['date']}")
        self.total_price.setText(f"Сумма: {self.order['total_price']}")
        self.user_data.setText(f"Пользователь: {self.order['user_surname']} {self.order['user_name']}")
        self.total_count.setText("")

    def on_click(self,event):
        from windows.Order_Items_Win import OrderItemsWindow
        if event.buttons() == QtCore.Qt.LeftButton:
            self.win = OrderItemsWindow(self.order,self)
            self.win.show()
    def remove_order(self):
        db.delete_order(self.order)
        self.deleteLater()