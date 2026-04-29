from src.product import Product


def test_init(product_one):
    """Тестирование класса Product"""

    assert product_one.name == "Iphone 15"
    assert product_one.description == "512GB, Gray space"
    assert product_one.price == 210000.0
    assert product_one.quantity == 8


def test_products(product_two):
    assert product_two.name == "Samsung Galaxy S23 Ultra"
    assert product_two.description == "256GB, Серый цвет, 200MP камера"
    assert product_two.price == 180000.0
    assert product_two.quantity == 5


def test_price_zero(product_one):

    product_one.price = 5000.0
    assert product_one.price == 5000.0
    product_one.price = -100
    assert product_one.price == 5000.0
    product_one.price = 0
    assert product_one.price == 5000.0


def test_product_total_sum():
    """Тестирование магического метода __add__"""
    p1 = Product("iPhone", "Apple phone", 100.0, 5)  # 100 * 5 = 500
    p2 = Product("Samsung", "Android phone", 200.0, 2)  # 400

    assert p1 + p2 == 900.0


def test_str(product_one):
    """Тестирование магического метода __str__"""
    assert str(product_one) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
