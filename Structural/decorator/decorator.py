from abc import abstractmethod, ABC


class Component(ABC):
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """

    @abstractmethod
    def execute(self):
        raise NotImplementedError


class Decorator(Component):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """

    __component: Component = None

    def __init__(self, component: Component):
        self.__component: Component = component

    @property
    def component(self):
        """
        The Decorator delegates all work to the wrapped component.
        """

        return self.__component

    def execute(self):
        return self.__component.execute()

