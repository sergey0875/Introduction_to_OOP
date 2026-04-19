def test_init_two(category_one):
    """Тестирование класса Category"""
    assert category_one.name == "Смартфоны"
    assert category_one.description == "Смартфоны для жизни"
    assert len(category_one.products) == 3
