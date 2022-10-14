import sqlite3

class Database:
    def __init__(self, db_path='shop_database.db'):
        self.db_path = db_path

    @property
    def connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, sql: str, parameters: tuple = tuple(),
                fetchone=False, fetchall=False, commit=False):  # fetchone - если мы делаем запрос и должна вернутся одна запись ,
                                                                # fetchall - если нужно из запроса несколько (все)
                                                                # commit - если вносим в БД изменения
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE users(
        id int NOT NULL,
        phone text,
        PRIMARY KEY (id)
        );
        """

        self.execute(sql, commit=True)

    def add_user(self, id: int, phone: str = None):
        sql = 'INSERT INTO users(id, phone) VALUES(?,?)'
        parameters = (id, phone)
        self.execute(sql, parameters, commit=True)

    def select_user_info(self, **kwargs) -> list:
        sql = 'SELECT * FROM users WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def select_all_users(self) -> list:
        sql = "SELECT * FROM users "
        return self.execute(sql, fetchall=True)

    def update_user_phone(self, id: int, phone: str):
        sql = "UPDATE users SET phone=? WHERE id=?"
        return self.execute(sql, parameters=(phone, id), commit=True)

    def delete_user(self, **kwargs):
        sql = "DELETE FROM users WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return self.execute(sql, parameters=parameters, commit=True)

    def delete_all(self):
        self.execute("DELETE FROM users WHERE True", commit=True)

    def drop_all(self):
        self.execute("DROP TABLE users", commit=True)

    @staticmethod
    def format_args(sql, parameters: dict) -> tuple:
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())



## ЗДЕСЬ СДЕЛАТЬ ТОВАРЫ
    def create_table_products(self):
        sql = """
        CREATE TABLE products(
        id int NOT NULL,
        title text,
        count int,
        photo_path text,
        PRIMARY KEY (id)
        );
        """

        self.execute(sql, commit=True)

    def add_product(self, id: int, title: str = None, count: int = 0, photo: str = ''):
        sql = 'INSERT INTO products(id, title, count, photo_path) VALUES(?,?,?)'
        parameters = (id, title, count, photo)
        self.execute(sql, parameters, commit=True)

    def select_product_info(self, **kwargs) -> list:
        sql = 'SELECT * FROM products WHERE '
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def select_all_products(self) -> list:
        sql = "SELECT * FROM products "
        return self.execute(sql, fetchall=True)

    def get_product_count(self) -> int:
        sql = "SELECT * FROM products"
        return len(self.execute(sql, fetchall=True))

    def update_product_count(self, count: int, title: str):
        sql = "UPDATE products SET title=? WHERE count=?"
        return self.execute(sql, parameters=(title, count), commit=True)

    def delete_all(self, **kwargs):
        sql = "DELETE FROM products WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return self.execute(sql, parameters=parameters, commit=True)

    def drop_all(self):
        self.execute("DROP FROM users", commit=True)
        self.execute("DROP TABLE products", commit=True)
