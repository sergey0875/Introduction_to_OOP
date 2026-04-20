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
