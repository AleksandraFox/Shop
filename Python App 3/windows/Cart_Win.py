from ui.Ui_cart_win import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QMessageBox
from db import db

class CartWindow(Ui_MainWindow,QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.cancel_btn.clicked.connect(lambda: self.close())
        self.create_order_btn.clicked.connect(self.create_order)
        self.load_widgets()

    def load_widgets(self):
        from windows.Product_In_Cart_Widget import ProductInCartWidget
        layout = self.scrollAreaWidgetContents.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        total_price = 0
        for c in db.cart:
            layout.addWidget(ProductInCartWidget(c,self))
            total_price += c['selected_count'] * c['price']

        self.total_price.setText(f"Сумма: {total_price}")
                

    def create_order(self):
        db.create_order(self.parent.user.id)
        self.close()