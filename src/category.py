from src.product import Product


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

        Category.product_count += len(products)   #счетчик категорий и товаров.
        Category.category_count += 1

    def add_product(self, product):
        if isinstance(product, Product): # Проверяем соответствует ли класс объекта.
                self.__products.append(product)
                Category.product_count += 1
        else:
            raise TypeError


    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)#Проходим циклом по количеству и суммируем
        return f"{self.name}, количество продуктов: {total_quantity} шт."


    @property
    def products(self):
        result = ""

        for product in self.__products:

            result += (
                f"{str(product)}\n"
            )

        return result


#
# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(str(product1))
#     print(str(product2))
#     print(str(product3))
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     print(str(category1))
#
#     print(category1.products)
#
#     print(product1 + product2)
#     print(product1 + product3)
#     print(product2 + product3)