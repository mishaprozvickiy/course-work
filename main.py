import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel
from ui_main import Ui_MainWindow
from new_transaction import Ui_Dialog
import error_window
from connection import Database


class Application(QMainWindow):
    def __init__(self):
        super(Application, self).__init__()
        self.window = Ui_MainWindow()
        self.window.setupUi(self)
        self.connection = Database()
        self.reload_data()
        self.view_database()
        self.window.new_transaction.clicked.connect(self.open_new_transaction_window)
        self.window.edit_transaction.clicked.connect(self.open_new_transaction_window)
        self.window.delete_transaction.clicked.connect(self.delete_current_transaction)
        self.new_window = None
        self.ui_window = None
        self.error_window = None
        self.ui_error_window = None
        self.model = None

    def view_database(self):
        self.model = QSqlTableModel(self)
        self.model.setTable("accounting")
        self.model.select()
        self.window.tableView.setModel(self.model)

    def reload_data(self):
        self.window.balance.setText(self.connection.total_balance())
        self.window.solved_balance.setText(self.connection.total_solved())
        self.window.not_solved_balance.setText(self.connection.total_not_solved())
        self.window.balance_phone.setText(self.connection.total_phone())
        self.window.balance_tablet.setText(self.connection.total_tablet())
        self.window.balance_labtop.setText(self.connection.total_labtop())
        self.window.balance_computer.setText(self.connection.total_computer())
        self.window.balance_other.setText(self.connection.total_other())

        self.window.all.setText(self.connection.count_all())
        self.window.count_solved.setText(self.connection.count_solved())
        self.window.count_not_solved.setText(self.connection.count_not_solved())
        self.window.count_phone.setText(self.connection.count_phone())
        self.window.count_tablet.setText(self.connection.count_tablet())
        self.window.count_labtop.setText(self.connection.count_labtop())
        self.window.count_computer.setText(self.connection.count_computer())
        self.window.count_other.setText(self.connection.count_other())

    def open_new_transaction_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()

        if sender.text() == "Новый заказ":
            self.ui_window.save_new_transaction.clicked.connect(self.add_new_transaction)

        else:
            self.ui_window.save_new_transaction.clicked.connect(self.edit_current_transaction)

    def add_new_transaction(self):
        date = self.ui_window.date.text()
        category = self.ui_window.choose_category.currentText()
        description = self.ui_window.description.text()
        balance = self.ui_window.balance.text()
        status = self.ui_window.status.currentText()

        try:
            if balance and category:
                int(balance)
                self.connection.add_new_transaction_query(date, category, description, balance, status)
                self.reload_data()
                self.view_database()
                self.new_window.close()

            elif not balance and category:
                self.open_error_window("Заполните поле\n'Стоимость заказа'!")

            elif balance and not category:
                self.open_error_window("Заполните поле\n'Вид ремонта'!")

            else:
                self.open_error_window("Заполните поля\n'Вид ремонта' и\n'Стоимость заказа'!")

        except ValueError:
            self.open_error_window("Поле 'Стоимость заказа'\nзаполнено некорректно!")

    def edit_current_transaction(self):
        index = self.window.tableView.selectedIndexes()

        if not index:
            self.new_window.close()
            return

        index = index[0]
        id = str(self.window.tableView.model().data(index))
        date = self.ui_window.date.text()
        category = self.ui_window.choose_category.currentText()
        description = self.ui_window.description.text()
        balance = self.ui_window.balance.text()
        status = self.ui_window.status.currentText()

        try:
            if balance and category:
                int(balance)
                self.connection.update_transaction_query(date, category, description, balance, status, id)
                self.reload_data()
                self.view_database()
                self.new_window.close()

            elif not balance and category:
                self.open_error_window("Заполните поле\n'Стоимость заказа'!")

            elif balance and not category:
                self.open_error_window("Заполните поле\n'Вид ремонта'!")

            else:
                self.open_error_window("Заполните поля\n'Вид ремонта' и\n'Стоимость заказа'!")

        except ValueError:
            self.open_error_window("Поле 'Стоимость заказа'\nзаполнено некорректно!")

    def delete_current_transaction(self):
        index = self.window.tableView.selectedIndexes()

        if not index:
            return

        index = index[0]
        id = str(self.window.tableView.model().data(index))
        self.connection.delete_transaction_query(id)
        self.reload_data()
        self.view_database()

    def open_error_window(self, error_message):
        self.error_window = QtWidgets.QDialog()
        self.ui_error_window = error_window.Ui_Dialog()
        self.ui_error_window.setupUi(self.error_window)
        self.error_window.show()
        self.ui_error_window.error_message.setText(error_message)
        self.ui_error_window.close_button.clicked.connect(self.close_window)

    def close_window(self):
        self.error_window.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())