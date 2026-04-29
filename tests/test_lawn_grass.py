def test_lawn_grass(category_three):
    assert category_three.country == "Россия"
    assert category_three.germination_period == "7 дней"
    assert category_three.description == "Элитная трава для газона"
    assert category_three.name == "Газонная трава"
    assert category_three.color == "Зеленый"
    assert category_three.price == 500.0
    assert category_three.quantity == 20


def test_lawn_grass2(category_three1):
    assert category_three1.country == "США"
    assert category_three1.germination_period == "5 дней"
    assert category_three1.description == "Выносливая трава"
    assert category_three1.name == "Газонная трава 2"
    assert category_three1.color == "Темно-зеленый"
    assert category_three1.price == 450.0
    assert category_three1.quantity == 15
