# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

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
        self.id_order = QLabel(Form)
        self.id_order.setObjectName(u"id_order")

        self.horizontalLayout_2.addWidget(self.id_order)

        self.date = QLabel(Form)
        self.date.setObjectName(u"date")

        self.horizontalLayout_2.addWidget(self.date)

        self.user_data = QLabel(Form)
        self.user_data.setObjectName(u"user_data")

        self.horizontalLayout_2.addWidget(self.user_data)

        self.total_count = QLabel(Form)
        self.total_count.setObjectName(u"total_count")

        self.horizontalLayout_2.addWidget(self.total_count)

        self.total_price = QLabel(Form)
        self.total_price.setObjectName(u"total_price")

        self.horizontalLayout_2.addWidget(self.total_price)

        self.delete_order_btn = QPushButton(Form)
        self.delete_order_btn.setObjectName(u"delete_order_btn")

        self.horizontalLayout_2.addWidget(self.delete_order_btn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.id_order.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.date.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.user_data.setText(QCoreApplication.translate("Form", u"\u0424\u0418\u041e", None))
        self.total_count.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e", None))
        self.total_price.setText(QCoreApplication.translate("Form", u"\u0421\u0443\u043c\u043c\u0430 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.delete_order_btn.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

