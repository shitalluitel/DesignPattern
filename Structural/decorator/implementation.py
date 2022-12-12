from Structural.decorator.decorator import Component, Decorator


class UserInput(Component):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.

    Here it helps to capture user input.
    """

    def __init__(self, text):
        self.text = text

    def execute(self):
        return self.text


class BoldDecorator(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """

    def execute(self):
        """
        Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.
        """
        return "<b>{}</b>".format(self.component.execute())


class ItalicDecorator(Decorator):
    """
    Decorators can execute their behavior either before or after the call to a
    wrapped object.
    """

    def execute(self):
        return "<i>{}</i>".format(self.component.execute())


class UnderLineDecorator(Decorator):
    def execute(self):
        return "<u>{}</u>".format(self.component.execute())


if __name__ == "__main__":
    normal_text = UserInput('My name is Shital Babu Luitel.')

    decorators = [BoldDecorator, ItalicDecorator]

    for decorator in decorators:
        normal_text = decorator(normal_text)

    print(normal_text.execute())
