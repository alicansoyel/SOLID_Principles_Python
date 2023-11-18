from abc import ABC, abstractmethod
import sqlite3
import mysql.connector

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def find(self, query):
        pass


class SQLiteDatabase(Database):
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def connect(self):
        print("Connected to SQLite database")

    def insert(self):
        print("Saving data")

    def find(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        print("Data found")
        return rows


class MySqlDatabase(Database):
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def connect(self):
        print("Connected to MySQL database")

    def insert(self):
        print("Saving data")

    def find(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        print("Data found")
        return rows


class DataManager:
    def __init__(self, database: Database):
        self.database = database

    def save_data(self):
        self.database.connect()
        self.database.insert()
    
    def find_data(self, query):
        self.database.connect()
        return self.database.find(query)


if __name__ == '__main__':
    sqlite_database = SQLiteDatabase("database_name.db")
    data_manager_sqlite = DataManager(sqlite_database)

    mysql_database = MySqlDatabase("your_mysql_host", "your_mysql_user", "your_mysql_password", "your_mysql_database")
    data_manager_mysql = DataManager(mysql_database)
