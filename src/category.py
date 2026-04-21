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
        self.__products = products

        Category.product_count += len(products)  # счетчик категорий и товаров.
        Category.category_count += 1

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        result = ""

        for product in self.__products:

            result += (
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            )

        return result
