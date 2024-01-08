# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(856, 673)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.balance_frame = QFrame(self.centralwidget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.balance_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.current_balance = QLabel(self.balance_frame)
        self.current_balance.setObjectName(u"current_balance")
        self.current_balance.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.current_balance.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.current_balance)

        self.balance = QLabel(self.balance_frame)
        self.balance.setObjectName(u"balance")
        self.balance.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.balance)

        self.all = QLabel(self.balance_frame)
        self.all.setObjectName(u"all")
        self.all.setStyleSheet(u"color: white;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.all)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.balance_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(30, 40))
        self.label_3.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_3.setPixmap(QPixmap(u":/icon/icons/solved.svg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_3)

        self.income = QLabel(self.balance_frame)
        self.income.setObjectName(u"income")
        self.income.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout.addWidget(self.income)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.solved_balance = QLabel(self.balance_frame)
        self.solved_balance.setObjectName(u"solved_balance")
        self.solved_balance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.solved_balance)

        self.count_solved = QLabel(self.balance_frame)
        self.count_solved.setObjectName(u"count_solved")
        self.count_solved.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.count_solved)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.balance_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(30, 40))
        self.label_6.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_6.setPixmap(QPixmap(u":/icon/icons/not_solved.svg"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.outcome = QLabel(self.balance_frame)
        self.outcome.setObjectName(u"outcome")
        self.outcome.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.outcome)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.not_solved_balance = QLabel(self.balance_frame)
        self.not_solved_balance.setObjectName(u"not_solved_balance")
        self.not_solved_balance.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.not_solved_balance)

        self.count_not_solved = QLabel(self.balance_frame)
        self.count_not_solved.setObjectName(u"count_not_solved")
        self.count_not_solved.setStyleSheet(u"color: white;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.count_not_solved)


        self.horizontalLayout_7.addWidget(self.balance_frame)

        self.categories_frame = QFrame(self.centralwidget)
        self.categories_frame.setObjectName(u"categories_frame")
        self.categories_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.categories_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.categories = QLabel(self.categories_frame)
        self.categories.setObjectName(u"categories")
        self.categories.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.categories.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.categories)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_10 = QLabel(self.categories_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(30, 30))
        self.label_10.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.label_10.setPixmap(QPixmap(u":/icon/icons/phone.svg"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_10)

        self.phone = QLabel(self.categories_frame)
        self.phone.setObjectName(u"phone")
        self.phone.setMinimumSize(QSize(0, 0))
        self.phone.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"width: 80;")

        self.horizontalLayout_6.addWidget(self.phone)

        self.balance_phone = QLabel(self.categories_frame)
        self.balance_phone.setObjectName(u"balance_phone")
        self.balance_phone.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.balance_phone)

        self.count_phone = QLabel(self.categories_frame)
        self.count_phone.setObjectName(u"count_phone")
        self.count_phone.setMaximumSize(QSize(100, 16777215))
        self.count_phone.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_6.addWidget(self.count_phone)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_15 = QLabel(self.categories_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(30, 30))
        self.label_15.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.label_15.setPixmap(QPixmap(u":/icon/icons/tablet.svg"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_15)

        self.tablet = QLabel(self.categories_frame)
        self.tablet.setObjectName(u"tablet")
        self.tablet.setMinimumSize(QSize(0, 0))
        self.tablet.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"width: 80;")

        self.horizontalLayout_5.addWidget(self.tablet)

        self.balance_tablet = QLabel(self.categories_frame)
        self.balance_tablet.setObjectName(u"balance_tablet")
        self.balance_tablet.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.balance_tablet)

        self.count_tablet = QLabel(self.categories_frame)
        self.count_tablet.setObjectName(u"count_tablet")
        self.count_tablet.setMaximumSize(QSize(100, 16777215))
        self.count_tablet.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.count_tablet)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_18 = QLabel(self.categories_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(30, 30))
        self.label_18.setSizeIncrement(QSize(0, 0))
        self.label_18.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.label_18.setPixmap(QPixmap(u":/icon/icons/labtop.svg"))
        self.label_18.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_18)

        self.labtop = QLabel(self.categories_frame)
        self.labtop.setObjectName(u"labtop")
        self.labtop.setMinimumSize(QSize(0, 0))
        self.labtop.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"width: 80;")

        self.horizontalLayout_4.addWidget(self.labtop)

        self.balance_labtop = QLabel(self.categories_frame)
        self.balance_labtop.setObjectName(u"balance_labtop")
        self.balance_labtop.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.balance_labtop)

        self.count_labtop = QLabel(self.categories_frame)
        self.count_labtop.setObjectName(u"count_labtop")
        self.count_labtop.setMaximumSize(QSize(100, 16777215))
        self.count_labtop.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.count_labtop)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_21 = QLabel(self.categories_frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(30, 30))
        self.label_21.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.label_21.setPixmap(QPixmap(u":/icon/icons/computer.svg"))
        self.label_21.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_21)

        self.computer = QLabel(self.categories_frame)
        self.computer.setObjectName(u"computer")
        self.computer.setMinimumSize(QSize(0, 0))
        self.computer.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"width: 80;")

        self.horizontalLayout_3.addWidget(self.computer)

        self.balance_computer = QLabel(self.categories_frame)
        self.balance_computer.setObjectName(u"balance_computer")
        self.balance_computer.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.balance_computer)

        self.count_computer = QLabel(self.categories_frame)
        self.count_computer.setObjectName(u"count_computer")
        self.count_computer.setMaximumSize(QSize(100, 16777215))
        self.count_computer.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.count_computer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_22 = QLabel(self.categories_frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(30, 30))
        self.label_22.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.label_22.setPixmap(QPixmap(u":/icon/icons/other.svg"))
        self.label_22.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_22)

        self.other = QLabel(self.categories_frame)
        self.other.setObjectName(u"other")
        self.other.setMinimumSize(QSize(0, 0))
        self.other.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: none;\n"
"border: none;\n"
"width: 80;")

        self.horizontalLayout_9.addWidget(self.other)

        self.balance_other = QLabel(self.categories_frame)
        self.balance_other.setObjectName(u"balance_other")
        self.balance_other.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_9.addWidget(self.balance_other)

        self.count_other = QLabel(self.categories_frame)
        self.count_other.setObjectName(u"count_other")
        self.count_other.setMaximumSize(QSize(100, 16777215))
        self.count_other.setStyleSheet(u"color: white;\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_9.addWidget(self.count_other)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_7.addWidget(self.categories_frame)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.new_transaction = QPushButton(self.centralwidget)
        self.new_transaction.setObjectName(u"new_transaction")
        self.new_transaction.setStyleSheet(u"QPushButton {\n"
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
        icon = QIcon()
        icon.addFile(u":/icon/icons/city.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.new_transaction.setIcon(icon)
        self.new_transaction.setIconSize(QSize(240, 240))

        self.horizontalLayout_8.addWidget(self.new_transaction)

        self.edit_transaction = QPushButton(self.centralwidget)
        self.edit_transaction.setObjectName(u"edit_transaction")
        self.edit_transaction.setStyleSheet(u"QPushButton {\n"
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
        self.edit_transaction.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.edit_transaction)

        self.delete_transaction = QPushButton(self.centralwidget)
        self.delete_transaction.setObjectName(u"delete_transaction")
        self.delete_transaction.setStyleSheet(u"QPushButton {\n"
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
        self.delete_transaction.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.delete_transaction)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"QTableView::section {\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"QTableView::item:selected {\n"
"border: none;\n"
"//color: rgba(255, 255, 255);\n"
"//background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0451\u0442 \u0440\u0435\u043c\u043e\u043d\u0442\u043d\u043e\u0439 \u043c\u0430\u0441\u0442\u0435\u0440\u0441\u043a\u043e\u0439", None))
        self.current_balance.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0441\u0443\u043c\u043c\u0430", None))
        self.balance.setText(QCoreApplication.translate("MainWindow", u"0 \u0440\u0443\u0431.", None))
        self.all.setText(QCoreApplication.translate("MainWindow", u"\u0432\u0441\u0435\u0433\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432: 0", None))
        self.label_3.setText("")
        self.income.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))
        self.solved_balance.setText(QCoreApplication.translate("MainWindow", u"0 \u0440\u0443\u0431.", None))
        self.count_solved.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043b-\u0432\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432: 0", None))
        self.label_6.setText("")
        self.outcome.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))
        self.not_solved_balance.setText(QCoreApplication.translate("MainWindow", u"0 \u0440\u0443\u0431.", None))
        self.count_not_solved.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043b-\u0432\u043e \u0437\u0430\u043a\u0430\u0437\u043e\u0432: 0", None))
        self.categories.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0434\u044b \u0440\u0435\u043c\u043e\u043d\u0442\u0430", None))
        self.label_10.setText("")
        self.phone.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043c\u043e\u043d\u0442\n"
"\u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.balance_phone.setText(QCoreApplication.translate("MainWindow", u"0 \u0440\u0443\u0431.", None))
        self.count_phone.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043b-\u0432\u043e: 0", None))
        self.label_15.setText("")
        self.tablet.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043c\u043e\u043d\u0442\n"
"\u043f\u043b\u0430\u043d\u0448\u0435\u0442\u0430", None))
        self.balance_tablet.setText(QCoreApplication.translate("MainWindow", u"0 \u0440\u0443\u0431.", None))
        self.count_tablet.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043b-\u0432\u043e: 0", None))
        self.label_18.setText("")
        self.labtop.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043c\u043e\u043d\u0442\n"
"\u043d\u043e\u0443\u0442\u0431\u0443\u043a\u0430", None))
        self.balance_labtop.setText(QCoreApplication.translate("MainWindow", u"0 \u0440\u0443\u0431.", None))
        self.count_labtop.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043b-\u0432\u043e: 0", None))
        self.label_21.setText("")
        self.computer.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043c\u043e\u043d\u0442\n"
"\u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430", None))
        self.balance_computer.setText(QCoreApplication.translate("MainWindow", u"0 \u0440\u0443\u0431.", None))
        self.count_computer.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043b-\u0432\u043e: 0", None))
        self.label_22.setText("")
        self.other.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043c\u043e\u043d\u0442\n"
"\u0434\u0440\u0443\u0433\u043e\u0439\n"
"\u0442\u0435\u0445\u043d\u0438\u043a\u0438", None))
        self.balance_other.setText(QCoreApplication.translate("MainWindow", u"0 \u0440\u0443\u0431.", None))
        self.count_other.setText(QCoreApplication.translate("MainWindow", u"\u043a\u043e\u043b-\u0432\u043e: 0", None))
        self.new_transaction.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0437\u0430\u043a\u0430\u0437", None))
        self.edit_transaction.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
        self.delete_transaction.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
    # retranslateUi

