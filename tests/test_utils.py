from unittest.mock import patch
from src.utils import creat_objects


def test_creat_objects_logic_isolation():
    data = [{"name": "Cat1", "products": [{"name": "Prod1"}]}]

    # Заменяем реальные классы на Mock-объекты
    with (
        patch("src.utils.Product") as MockProduct,
        patch("src.utils.Category") as MockCategory,
    ):
        creat_objects(data)

        # Проверяем, вызывались ли конструкторы нужных классов
        MockProduct.assert_called_once_with(name="Prod1")
        MockCategory.assert_called_once()
