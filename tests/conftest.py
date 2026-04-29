import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.product_iterator import ProductIterator
from src.smartphone import Smartphone


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


@pytest.fixture()
def product_two():
    return Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )


@pytest.fixture()
def category_two():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture()
def product_iterator(category_one):
    return ProductIterator(category_one)


@pytest.fixture()
def product_three():
    return Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        "Синий",
        90.3,
        "Note 11",
        1024,
        14,
    )


@pytest.fixture()
def product_three1():
    return Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )


@pytest.fixture()
def category_three():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


@pytest.fixture()
def category_three1():
    return LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
