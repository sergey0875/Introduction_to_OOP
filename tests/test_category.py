from src.category import Category

def test_init_two(category_one):
    """Тестирование класса Category"""
    assert category_one.name == "Смартфоны"
    assert category_one.description == "Смартфоны для жизни"
    assert len(category_one._Category__products) == 3


def test_category_two(category_two):
    assert category_two.name == "Samsung Galaxy S23 Ultra"
    assert category_two.description == "256GB, Серый цвет, 200MP камера"
    assert category_two.price == 180000.0
    assert category_two.quantity == 5


def test_add_product(category_one, product_one):
    initial_count = Category.product_count
    category_one.add_product(product_one)

    assert len(category_one._Category__products) == 4
    assert Category.product_count == initial_count + 1



def test_category_str(category_one):
    """Тестирование магического метода __str__"""
    assert str(category_one) == "Смартфоны, количество продуктов: 27 шт."
