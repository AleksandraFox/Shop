# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product_win.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 730)
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

        self.img = QLabel(self.header)
        self.img.setObjectName(u"img")
        self.img.setMaximumSize(QSize(150, 150))
        self.img.setPixmap(QPixmap(u"../img/picture.png"))
        self.img.setScaledContents(True)

        self.horizontalLayout.addWidget(self.img)


        self.verticalLayout_2.addWidget(self.header, 0, Qt.AlignmentFlag.AlignTop)

        self.verticalWidget = QWidget(self.body)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout_3 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.name = QLabel(self.verticalWidget)
        self.name.setObjectName(u"name")
        self.name.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.name, 0, Qt.AlignmentFlag.AlignHCenter)

        self.manufacture = QLabel(self.verticalWidget)
        self.manufacture.setObjectName(u"manufacture")
        self.manufacture.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.manufacture, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addWidget(self.verticalWidget, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalWidget_2 = QWidget(self.body)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        self.verticalLayout_5 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.cat = QLabel(self.verticalWidget_2)
        self.cat.setObjectName(u"cat")
        self.cat.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.cat)

        self.description = QLabel(self.verticalWidget_2)
        self.description.setObjectName(u"description")
        self.description.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.description)

        self.structure = QLabel(self.verticalWidget_2)
        self.structure.setObjectName(u"structure")
        self.structure.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.structure)


        self.horizontalLayout_2.addWidget(self.verticalWidget_2, 0, Qt.AlignmentFlag.AlignLeft)

        self.verticalWidget1 = QWidget(self.body)
        self.verticalWidget1.setObjectName(u"verticalWidget1")
        self.verticalLayout_4 = QVBoxLayout(self.verticalWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scat = QLabel(self.verticalWidget1)
        self.scat.setObjectName(u"scat")
        self.scat.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.scat)

        self.total_count = QLabel(self.verticalWidget1)
        self.total_count.setObjectName(u"total_count")
        self.total_count.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.total_count)

        self.price = QLabel(self.verticalWidget1)
        self.price.setObjectName(u"price")
        self.price.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.price)


        self.horizontalLayout_2.addWidget(self.verticalWidget1, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.size_box = QComboBox(self.body)
        self.size_box.setObjectName(u"size_box")

        self.verticalLayout_2.addWidget(self.size_box)

        self.count_spin = QSpinBox(self.body)
        self.count_spin.setObjectName(u"count_spin")
        self.count_spin.setMinimum(1)

        self.verticalLayout_2.addWidget(self.count_spin)

        self.to_cart_btn = QPushButton(self.body)
        self.to_cart_btn.setObjectName(u"to_cart_btn")

        self.verticalLayout_2.addWidget(self.to_cart_btn)

        self.cancel_btn = QPushButton(self.body)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.verticalLayout_2.addWidget(self.cancel_btn)

        MainWindow.setCentralWidget(self.body)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0443\u0434\u043e \u043e\u0431\u0443\u0432\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.img.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.manufacture.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.cat.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.description.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.structure.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u0430\u0432", None))
        self.scat.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.total_count.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e", None))
        self.price.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430", None))
        self.count_spin.setPrefix(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e: ", None))
        self.to_cart_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043a\u043e\u0440\u0437\u0438\u043d\u0443", None))
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

