# The strategy interface declares operations common to all
# supported versions of some algorithm. The context uses this
# interface to call the algorithm defined by the concrete
# strategies.
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError


# The context defines the interface of interest to clients.
class Context:
    # The context maintains a reference to one of the strategy
    # objects. The context doesn't know the concrete class of a
    # strategy. It should work with all strategies via the
    # strategy interface.
    def __init__(self, strategy: Strategy = None):
        self.__strategy = strategy or Strategy

    # Usually the context accepts a strategy through the
    # constructor, and also provides a setter so that the
    # strategy can be switched at runtime.
    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self.__strategy = strategy

    # The context delegates some work to the strategy object
    # instead of implementing multiple versions of the
    # algorithm on its own.
    def execute_strategy(self, a: int, b: int):
        strategy_class = self.strategy
        return strategy_class().execute(a, b)
