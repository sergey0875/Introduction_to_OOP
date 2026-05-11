import pytest

from tests.conftest import category_three


def test_smartphone(product_three):
    assert product_three.name == "Xiaomi Redmi Note 11"
    assert product_three.description == "1024GB, Синий"
    assert product_three.price == 31000.0
    assert product_three.quantity == 14
    assert product_three.efficiency == 90.3
    assert product_three.model == "Note 11"
    assert product_three.memory == 1024
    assert product_three.color == "Синий"


def test_fvv(product_three, product_three1):
    with pytest.raises(TypeError):  # Ожидаем ошибку при сложении разных типов
        _ = product_three + category_three
