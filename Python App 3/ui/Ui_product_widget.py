# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1112, 355)
        Form.setStyleSheet(u"*{\n"
"	font: 24pt \"Calibri\";\n"
"	color:#70B2AF;\n"
"}\n"
"#header{\n"
"	background-color:#D2F6E7;\n"
"}\n"
"#Form{\n"
"	border:5px solid #D2F6E7;\n"
"	background-color:#fff;\n"
"}\n"
"#Form:hover{\n"
"	background-color:#D2F6E7;\n"
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
"}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalWidget = QWidget(Form)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.img = QLabel(self.horizontalWidget)
        self.img.setObjectName(u"img")
        self.img.setMaximumSize(QSize(100, 100))
        self.img.setPixmap(QPixmap(u"../img/picture.png"))
        self.img.setScaledContents(True)

        self.horizontalLayout.addWidget(self.img)

        self.verticalWidget = QWidget(self.horizontalWidget)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalLayout = QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.cat = QLabel(self.verticalWidget)
        self.cat.setObjectName(u"cat")
        self.cat.setWordWrap(True)

        self.verticalLayout.addWidget(self.cat)

        self.structure = QLabel(self.verticalWidget)
        self.structure.setObjectName(u"structure")
        self.structure.setWordWrap(True)

        self.verticalLayout.addWidget(self.structure)

        self.total_count = QLabel(self.verticalWidget)
        self.total_count.setObjectName(u"total_count")
        self.total_count.setWordWrap(True)

        self.verticalLayout.addWidget(self.total_count)


        self.horizontalLayout.addWidget(self.verticalWidget)


        self.horizontalLayout_2.addWidget(self.horizontalWidget, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalWidget_2 = QWidget(Form)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.name = QLabel(self.horizontalWidget_2)
        self.name.setObjectName(u"name")
        self.name.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.name, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_2.addWidget(self.horizontalWidget_2)

        self.horizontalWidget_3 = QWidget(Form)
        self.horizontalWidget_3.setObjectName(u"horizontalWidget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.price = QLabel(self.horizontalWidget_3)
        self.price.setObjectName(u"price")
        self.price.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.price, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.horizontalWidget_3, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.img.setText("")
        self.cat.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.structure.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0441\u0442\u0430\u0432", None))
        self.total_count.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e", None))
        self.name.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435|\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c", None))
        self.price.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430", None))
    # retranslateUi

