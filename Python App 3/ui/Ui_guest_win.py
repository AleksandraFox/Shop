# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guest_win.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
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
"}\n"
"QScrollArea{\n"
"	background-color:#fff;\n"
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

        self.logount_btn = QPushButton(self.header)
        self.logount_btn.setObjectName(u"logount_btn")

        self.horizontalLayout.addWidget(self.logount_btn)


        self.verticalLayout_2.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea = QScrollArea(self.body)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 780, 18))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        MainWindow.setCentralWidget(self.body)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0443\u0434\u043e \u043e\u0431\u0443\u0432\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0430", None))
        self.logount_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
    # retranslateUi

