from ui.Ui_order_items_win import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QMessageBox
from db import db

class OrderItemsWindow(Ui_MainWindow,QMainWindow):
    def __init__(self,order, parent = None):
        super().__init__(parent)
        self.parent = parent
        self.order = order
        self.setupUi(self)
        self.load_widgets()
        self.logount_btn.clicked.connect(lambda:self.close())
    def load_widgets(self):
        from windows.Order_Item_Widget import OrderItemWidget
        layout = self.scrollAreaWidgetContents.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
        for oi in self.order['order_items']:
            layout.addWidget(OrderItemWidget(oi,self))