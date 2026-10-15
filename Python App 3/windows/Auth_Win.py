from ui.Ui_auth_win import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow,QMessageBox
from db import db

class AuthWindow(Ui_MainWindow,QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.login_btn.clicked.connect(self.login)
        self.guest_btn.clicked.connect(self.guest)


    def login(self):
        user = db.get_user(self.login_input.text())
        if user:
            if user.roles.name == 'Авторизованный пользователь':
                from windows.User_Win import UserWindow
                self.win = UserWindow(user)
                self.win.show()
                self.close()
            elif user.roles.name == 'Менеджер':
                from windows.Manager_Win import ManagerWindow
                self.win = ManagerWindow(user)
                self.win.show()
                self.close()
            elif user.roles.name == 'Администратор':
                pass
        else:
            QMessageBox.warning(self,'Ошибка','Пользователь не найден')
    def guest(self):
        from windows.Guest_Win import GuestWindow
        self.win = GuestWindow()
        self.win.show()
        self.close()