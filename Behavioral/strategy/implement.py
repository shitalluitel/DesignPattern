# Concrete strategies implement the algorithm while following
# the base strategy interface. The interface makes them
# interchangeable in the context.
from DesignPattern.Behavioral.strategy.strategy import Strategy, Context


class ConcreteStrategyAdd(Strategy):
    def execute(self, a, b):
        return a + b


class ConcreteStrategySubtract(Strategy):
    def execute(self, a, b):
        return a - b


class ConcreteStrategyMultiply(Strategy):
    def execute(self, a, b):
        return a * b


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
