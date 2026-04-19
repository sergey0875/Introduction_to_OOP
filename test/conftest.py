import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product_one():
    return Product(
        name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8
    )


@pytest.fixture()
def category_one():

    p1 = Product("Samsung S23", "256GB", 180000.0, 5)
    p2 = Product("Iphone 15", "512GB", 210000.0, 8)
    p3 = Product("Xiaomi", "1024GB", 31000.0, 14)

    return Category(
        name="Смартфоны", description="Смартфоны для жизни", products=[p1, p2, p3]
    )
