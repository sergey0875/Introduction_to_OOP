class Category:
    """Класс для представления категории."""

    product_count = 0
    category_count = 0
    name: str
    description: str
    products: str

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.products = products

        Category.product_count += len(products)  # счетчик категорий и товаров.
        Category.category_count += 1
