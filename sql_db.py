import sqlite3
import time
class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    #_____________________________Добавление юзера_________________________--
    def examination(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchall()
            return bool(len(res))

    def add(self, user_id, ref_id=None):
        with self.connection:
            if ref_id != None:
                return self.connection.execute("INSERT INTO users ('user_id' , 'ref_id') VALUES (?,?)", (user_id,ref_id,))
            else:
                return self.connection.execute("INSERT INTO users ('user_id') VALUES (?)", (user_id,))

    def user_shop(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT shop FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_shop(self, user_id, shop):
        with self.connection:
            return self.cursor.execute("UPDATE users SET shop = ? WHERE user_id = ?", (shop, user_id))

    def user_name(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT name FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return res[0][0]

    def add_name(self, user_id, name):
        with self.connection:
            return self.cursor.execute("UPDATE users SET name = ? WHERE user_id = ?", (name, user_id))

    def user_number(self, user_id):
        with self.connection:
            res = self.cursor.execute("SELECT number FROM users WHERE user_id = ?", (user_id,)).fetchmany(1)
            return int(res[0][0])

    def add_number(self, user_id, number):
        with self.connection:
            return self.cursor.execute("UPDATE users SET number = ? WHERE user_id = ?", (number, user_id))
