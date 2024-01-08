# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(440, 384)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.transaction = QLabel(self.frame)
        self.transaction.setObjectName(u"transaction")
        self.transaction.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.transaction.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.transaction)

        self.choose_category = QComboBox(self.frame)
        self.choose_category.addItem("")
        self.choose_category.addItem("")
        self.choose_category.addItem("")
        self.choose_category.addItem("")
        self.choose_category.addItem("")
        self.choose_category.setObjectName(u"choose_category")
        self.choose_category.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"QComboBox:item {\n"
"color: black\n"
"}")

        self.verticalLayout.addWidget(self.choose_category)

        self.status = QComboBox(self.frame)
        self.status.addItem("")
        self.status.addItem("")
        self.status.setObjectName(u"status")
        self.status.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"QComboBox:item {\n"
"color: black\n"
"}")

        self.verticalLayout.addWidget(self.status)

        self.date = QDateEdit(self.frame)
        self.date.setObjectName(u"date")
        self.date.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")
        self.date.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date.setDate(QDate(2023, 1, 1))

        self.verticalLayout.addWidget(self.date)

        self.description = QLineEdit(self.frame)
        self.description.setObjectName(u"description")
        self.description.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.description)

        self.balance = QLineEdit(self.frame)
        self.balance.setObjectName(u"balance")
        self.balance.setStyleSheet(u"font-size: 16pt;\n"
"color: white;\n"
"padding-left: 10px;")

        self.verticalLayout.addWidget(self.balance)

        self.save_new_transaction = QPushButton(self.frame)
        self.save_new_transaction.setObjectName(u"save_new_transaction")
        self.save_new_transaction.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")

        self.verticalLayout.addWidget(self.save_new_transaction)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.choose_category.setCurrentIndex(-1)
        self.status.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.transaction.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0430\u0437", None))
        self.choose_category.setItemText(0, QCoreApplication.translate("Dialog", u"\u0420\u0435\u043c\u043e\u043d\u0442 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.choose_category.setItemText(1, QCoreApplication.translate("Dialog", u"\u0420\u0435\u043c\u043e\u043d\u0442 \u043f\u043b\u0430\u043d\u0448\u0435\u0442\u0430", None))
        self.choose_category.setItemText(2, QCoreApplication.translate("Dialog", u"\u0420\u0435\u043c\u043e\u043d\u0442 \u043d\u043e\u0443\u0442\u0431\u0443\u043a\u0430", None))
        self.choose_category.setItemText(3, QCoreApplication.translate("Dialog", u"\u0420\u0435\u043c\u043e\u043d\u0442 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430", None))
        self.choose_category.setItemText(4, QCoreApplication.translate("Dialog", u"\u0420\u0435\u043c\u043e\u043d\u0442 \u0434\u0440\u0443\u0433\u043e\u0439 \u0442\u0435\u0445\u043d\u0438\u043a\u0438", None))

        self.choose_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434 \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
        self.status.setItemText(0, QCoreApplication.translate("Dialog", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d", None))
        self.status.setItemText(1, QCoreApplication.translate("Dialog", u"\u041d\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d", None))

        self.description.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.save_new_transaction.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
    # retranslateUi

