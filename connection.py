from PySide6 import QtWidgets, QtSql


class Database:
    def __init__(self):
        super(Database, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("accounting_database.db")

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Не получилось открыть базу данных", "Нажмите 'Cancel' для выхода", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS accounting (ID integer primary key AUTOINCREMENT, Date VARCHAR(20), Category VARCHAR(20), Description VARCHAR(20), Balance REAL, Status VARCHAR(20))")
        return True

    def execute_query_with_params(self, sql_query, query_values = None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def add_new_transaction_query(self, date, category, description, balance, status):
        sql_query = "INSERT INTO accounting (Date, Category, Description, Balance, Status) VALUES (?, ?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status])

    def update_transaction_query(self, date, category, description, balance, status, id):
        sql_query = "UPDATE accounting SET Date = ?, Category = ?, Description = ?, Balance = ?, Status = ? WHERE ID = ?"
        self.execute_query_with_params(sql_query, [date, category, description, balance, status, id])

    def delete_transaction_query(self, id):
        sql_query = "DELETE FROM accounting WHERE ID = ? AND Status = ?"
        self.execute_query_with_params(sql_query, [id, "Не выполнен"])

    def get_total(self, column, filter = None, value = None):
        sql_query = f"SELECT SUM ({column}) FROM accounting"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"
        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)
        if query.next() and query.value(0):
            return str(int(query.value(0))) + " руб."
        return "0 руб."

    def total_balance(self):
        return self.get_total("Balance")

    def total_solved(self):
        return self.get_total("Balance", "Status", "Выполнен")

    def total_not_solved(self):
        return self.get_total("Balance", "Status", "Не выполнен")

    def total_phone(self):
        return self.get_total("Balance", "Category", "Ремонт телефона")

    def total_tablet(self):
        return self.get_total("Balance", "Category", "Ремонт планшета")

    def total_labtop(self):
        return self.get_total("Balance", "Category", "Ремонт ноутбука")

    def total_computer(self):
        return self.get_total("Balance", "Category", "Ремонт компьютера")

    def total_other(self):
        return self.get_total("Balance", "Category", "Ремонт другой техники")

    def get_count(self, column, filter = None, value = None):
        sql_query = f"SELECT COUNT ({column}) FROM accounting"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"
        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next() and query.value(0):
            return "кол-во заказов: " + str(query.value(0))
        return "кол-во заказов: 0"

    def get_count2(self, column, filter = None, value = None):
        sql_query = f"SELECT COUNT ({column}) FROM accounting"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"
        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next() and query.value(0):
            return "кол-во: " + str(query.value(0))
        return "кол-во: 0"

    def get_count3(self, column, filter = None, value = None):
        sql_query = f"SELECT COUNT ({column}) FROM accounting"

        if filter is not None and value is not None:
            sql_query += f" WHERE {filter} = ?"
        query_values = []

        if value is not None:
            query_values.append(value)

        query = self.execute_query_with_params(sql_query, query_values)

        if query.next() and query.value(0):
            return "всего заказов: " + str(query.value(0))
        return "всего заказов: 0"

    def count_all(self):
        return self.get_count3("Balance")

    def count_solved(self):
        return self.get_count("Balance", "Status", "Выполнен")

    def count_not_solved(self):
        return self.get_count("Balance", "Status", "Не выполнен")

    def count_phone(self):
        return self.get_count2("Balance", "Category", "Ремонт телефона")

    def count_tablet(self):
        return self.get_count2("Balance", "Category", "Ремонт планшета")

    def count_labtop(self):
        return self.get_count2("Balance", "Category", "Ремонт ноутбука")

    def count_computer(self):
        return self.get_count2("Balance", "Category", "Ремонт компьютера")

    def count_other(self):
        return self.get_count2("Balance", "Category", "Ремонт другой техники")