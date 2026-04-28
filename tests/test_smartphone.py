import pytest


def test_smartphone(product_three):
    assert product_three.name == 90.3
    assert product_three.description =="Note 11"
    assert product_three.efficiency == "Xiaomi Redmi Note 11"
    assert product_three.model == "1024GB, Синий"
    assert product_three.memory == 31000.0
    assert product_three.color == "Синий"
    assert product_three.price == 1024
    assert product_three.quantity == 14




def test_fvv(product_three, product_three1):
    with pytest.raises(TypeError):  # Ожидаем ошибку при сложении разных типов
        result = product_three + product_three1

