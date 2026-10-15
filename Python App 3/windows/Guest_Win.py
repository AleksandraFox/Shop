from ui.Ui_guest_win import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QMessageBox
from db import db

class GuestWindow(Ui_MainWindow,QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.is_guest = True
        self.load_widgets()
        self.logount_btn.clicked.connect(self.logout)


    def load_widgets(self):
        from windows.Product_Widget import ProductWidget
        layout = self.scrollAreaWidgetContents.layout()
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for p in db.all_products:
            if not p['hidden']:
                layout.addWidget(ProductWidget(p,self))

    def logout(self):
        from windows.Auth_Win import AuthWindow
        self.win = AuthWindow()
        self.win.show()
        self.close()