from ui.Ui_orders_win import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QMessageBox
from db import db

class OrdersWindow(Ui_MainWindow,QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.logout_btn.clicked.connect(lambda: self.close())
        self.load_widgets()

    def load_widgets(self):
        from windows.Order_Widget import OrderWidget
        layout = self.scrollAreaWidgetContents.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for o in db.group_orders():
            layout.addWidget(OrderWidget(o,self))