from itertools import product




class Product:
    """Класс для представления продукта."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if type(other) is Product: # Проверяем тип класса. Если класс другой возбуждаем исключение
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError


    @classmethod
    def new_product(
        cls, product_data
    ):  #Класс-метод для получения значений из словаря по ключу
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        return cls(name, description, price, quantity)

    @property
    def price(self):  # Геттер возвращает цену
        return self.__price

    @price.setter
    def price(self, new_price):

        # Сеттер для проверки цены
        if new_price <= 0:
              print("Цена не должна быть нулевая или отрицательная")

        else:
            self.__price = new_price




