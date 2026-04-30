class Mixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        """Класс-миксин для вывода от какого класса и с какими параметрами был создан объект."""
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
