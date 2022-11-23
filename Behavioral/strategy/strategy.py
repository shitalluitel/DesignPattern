# The strategy interface declares operations common to all
# supported versions of some algorithm. The context uses this
# interface to call the algorithm defined by the concrete
# strategies.
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        raise NotImplementedError


# Concrete strategies implement the algorithm while following
# the base strategy interface. The interface makes them
# interchangeable in the context.

class ConcreteStrategyAdd(Strategy):
    def execute(self, a, b):
        return a + b


class ConcreteStrategySubtract(Strategy):
    def execute(self, a, b):
        return a - b


class ConcreteStrategyMultiply(Strategy):
    def execute(self, a, b):
        return a * b


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


# The client code picks a concrete strategy and passes it to
# the context. The client should be aware of the differences
# between strategies in order to make the right choice.


if __name__ == '__main__':
    # Create context object.
    context = Context()

    # Read first number.
    first = input('First Number: ')
    # Read last number.
    last = input('Last Number: ')

    print(
        """
Available action:
    1: Addition
    2. Subtraction
    3. Multiplication  
"""
    )
    # Read the desired action from user input.
    action = input('Selected Action: ')

    action_map = {
        '1': ConcreteStrategyAdd,
        '2': ConcreteStrategySubtract,
        '3': ConcreteStrategyMultiply
    }
    context.strategy = action_map[action]
    result = context.execute_strategy(int(first), int(last))

    print(result)
