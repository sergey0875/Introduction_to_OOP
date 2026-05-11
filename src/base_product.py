from abc import ABC
from abc import abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """Общая функция абстрактонго метода"""
        pass
