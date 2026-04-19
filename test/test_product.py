def test_init(product_one):
    """Тестирование класса Product"""

    assert product_one.name == "Iphone 15"
    assert product_one.description == "512GB, Gray space"
    assert product_one.price == 210000.0
    assert product_one.quantity == 8
