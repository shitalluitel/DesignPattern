"""The Chair Interface"""
from abc import ABCMeta, abstractmethod

"""
The creator class declares the factory method that must return an object of 
a product class. The creator's subclasses usually provide the implementation 
of this method.
"""


class IChair(metaclass=ABCMeta):
    """The creator may also provide some default implementation of the factory method."""

    @staticmethod
    @abstractmethod
    def get_dimensions():
        """
         Note that, despite its name, the creator's primary responsibility isn't creating products. It usually contains
         some core business logic that relies on product objects returned by the factory method. Subclasses can
         indirectly change that business logic by overriding the factory method and returning a different type of
         product from it.
        """


class SmallChair(IChair):
    """The Small Chair Concrete Class implements the IChair interface"""

    def __init__(self):
        self._height = 40
        self._width = 40
        self._depth = 40

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }


class MediumChair(IChair):
    """The Medium Chair Concrete Class implements the IChair interface"""

    def __init__(self):
        self._height = 60
        self._width = 60
        self._depth = 60

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }


class BigChair(IChair):
    """The Big Chair Concrete Class implements the IChair interface"""

    def __init__(self):
        self._height = 80
        self._width = 80
        self._depth = 80

    def get_dimensions(self):
        return {
            "width": self._width,
            "depth": self._depth,
            "height": self._height
        }


class ChairFactory:
    """
        The client code works with an instance of a concrete creator, albeit through its base interface.As long as
        the client keeps working with the creator via the base interface, you can pass it any creator 's subclass.
    """

    __klass_map = {
        '1': SmallChair,
        '2': MediumChair,
        '3': BigChair
    }

    def __new__(cls, _filter):
        """
        The application picks a creator's type depending on the
        current configuration or environment settings.
        """
        klass_map = cls.__klass_map
        klass = klass_map.get(_filter)
        if klass:
            return klass()
        raise ModuleNotFoundError


# The Client
print(
    """
    Chair Type:
    1. Small Chair
    2. Medium Chair
    3. Big Chair
    """.center(20)
)
chair_type = input('Chair Type: ')
CHAIR = ChairFactory(chair_type)
print(CHAIR.get_dimensions())
