# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth_win.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"*{\n"
"	font: 24pt \"Calibri\";\n"
"	color:#70B2AF;\n"
"}\n"
"#header{\n"
"	background-color:#D2F6E7;\n"
"}\n"
"#body{\n"
"	background-color:#fff;\n"
"}\n"
"QPushButton{\n"
"	background-color:#70B2AF;\n"
"	color:#D2F6E7;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#D2F6E7;\n"
"	color:#70B2AF;\n"
"}")
        self.body = QWidget(MainWindow)
        self.body.setObjectName(u"body")
        self.verticalLayout_2 = QVBoxLayout(self.body)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.header = QWidget(self.body)
        self.header.setObjectName(u"header")
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.header)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(100, 100))
        self.label_4.setPixmap(QPixmap(u"../img/\u0427\u0443\u0434\u043e \u041e\u0431\u0443\u0432\u044c.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.header)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.header)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.body)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.login_input = QLineEdit(self.body)
        self.login_input.setObjectName(u"login_input")

        self.verticalLayout_3.addWidget(self.login_input)

        self.login_btn = QPushButton(self.body)
        self.login_btn.setObjectName(u"login_btn")

        self.verticalLayout_3.addWidget(self.login_btn)

        self.guest_btn = QPushButton(self.body)
        self.guest_btn.setObjectName(u"guest_btn")

        self.verticalLayout_3.addWidget(self.guest_btn)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.body)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0443\u0434\u043e \u043e\u0431\u0443\u0432\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.guest_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438 \u043a\u0430\u043a \u0433\u043e\u0441\u0442\u044c", None))
    # retranslateUi

