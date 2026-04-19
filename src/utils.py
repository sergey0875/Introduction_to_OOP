import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Функция чтения json файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def creat_objects(data):
    """Инициализирует объекты Category и Product из списка словарей."""
    categories = []
    for user in data:
        products_list = []
        for product in user["products"]:
            products_list.append(Product(**product))
        user["products"] = products_list
        categories.append(Category(**user))
    return categories


# if __name__ == "__main__":
#
#     raw_data = read_json("../data/products.json")
#     user_data = creat_objects(raw_data)
#     print(user_data[1].name)
#     print(user_data[1].products)
