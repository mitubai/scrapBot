import sqlite3
from pathlib import Path
from pprint import pprint


class Database:

    def __init__(self) -> None:
        db_path = Path(__file__).parent.parent / "database.sqlite"
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()

    def drop_tables(self):
        self.cursor.execute("DROP TABLE IF EXISTS dishes")
        self.db.commit()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS dish_categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                introduction_text TEXT
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS dishes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                price INTEGER,
                picture TEXT,
                category_id INTEGER,
                FOREIGN KEY(category_id) REFERENCES dish_categories(id)
            )
            """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS survey (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                phone_number TEXT
            )
            """
        )
        self.db.commit()

    def populate_tables(self):
        self.cursor.execute(
            """
            INSERT INTO dish_categories (name, introduction_text)
                VALUES  ('Пицца 30 см', 'Вот самые популярные пиццы'),
                        ('Пицца 40 см', 'Вот самые популярные пиццы 40 см'),
                        ('Закуски', 'Вот самые популярные закуски'), 
                        ('Салаты', 'Вот самые популярные салаты'), 
                        ('Супы', 'Вот самые популярные супы')
            """
        )
        self.cursor.execute(
            """
            INSERT INTO dishes (name, description, price, picture, category_id)  
                VALUES ('Пицца маргарита', 'Самый вкусный среди всех', 1699, 'pizza.jpg', 1),
               ('Пицца пеперони сырная', 'Пеперонни 40 см но с более сырной начинкой', 3400, 'pizza40.jpg', 2),
               ('Пицца пеперони классическая', 'Классическая пеперонни 40 см', 2900, '2pizza40.jpg', 2),
               ('Шоколадный труфель', 'Внутри тающий шоколад', 1700, 'dessert.jpg', 3),
               ('Шоколадные пряники', 'Очень хорошо подойдут с чаем', 700, '2dessert.png', 3),
               ('Классический овощной салад', 'Для тех кто на диете', 800, '1salad.jpg', 4),
               ('Фруктовый салад', 'Для любителей сладкого', 900, '2salad.jpg', 4),
               ('Шорпо', 'Классический-кыргызский суп', 1050, 'soap.jpg', 5),
               ('Том Ям', 'Острый-корейский суп, для любителей морепродуктов и острого', 1000, '2soap.jpg', 5)
            """
        )
        self.db.commit()

    def get_category_by_name(self, name: str):
        self.cursor.execute(
            "SELECT * FROM dish_categories WHERE name = :catName",
            {"catName": name},
        )
        return self.cursor.fetchone()

    def get_all_dishes(self):
        self.cursor.execute("SELECT * FROM dishes")
        return self.cursor.fetchall()

    def get_one_dish(self, id: int):
        self.cursor.execute(
            "SELECT * FROM dishes WHERE id = :dishId", {"dishId": id}
        )
        return self.cursor.fetchone()

    def get_cheap_dishes(self):
        self.cursor.execute("SELECT * FROM dishes WHERE price < 500")
        return self.cursor.fetchall()

    def get_dishes_by_category(self, category_id: int):
        self.cursor.execute(
            "SELECT * FROM dishes WHERE category_id = :categoryId",
            {"categoryId": category_id},
        )
        return self.cursor.fetchall()

    def get_dishes_by_cat_name(self, cat_name: str):
        self.cursor.execute(
            """
            SELECT d.* , dc.name FROM dishes AS d
            JOIN dish_categories AS dc ON d.category_id = dc.id
            WHERE dc.name = :catName
            """,
            {"catName": cat_name},
        )
        return self.cursor.fetchall()

    def insert_survey(self, data: dict):
        self.cursor.execute(
            """
            INSERT INTO survey (name, age, phone_number)
                VALUES (:name, :age, :phone_number)
            """,
            data,
        )
        self.db.commit()


if __name__ == "__main__":
    db = Database()
    #db.drop_tables()
    db.create_tables()
    #db.populate_tables()