from PySide6.QtWidgets import QApplication
from windows.Auth_Win import AuthWindow
                
app = QApplication([])
win = AuthWindow()
win.show()
app.exec()