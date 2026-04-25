import pytest

def test_product_iterator(product_iterator):
    """Тестирование класса ProductIterator"""
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung S23"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi"

    with pytest.raises(StopIteration): # Тестируем возбуждение исключения
        next(product_iterator)