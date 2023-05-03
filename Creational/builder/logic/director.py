"""
Controls the construction process.

Director has a builder associated with him. Director then
delegates building of the smaller parts to the builder and
assembles them together.
"""


class Car:
    """

    The final product.

    A car is assembled by the `Director' class from
    parts made by `Builder'. Both these classes have
    influence on the resulting object.

    """

    def __init__(self, company):
        self.__company = company
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body):
        self.__body = body

    @property
    def wheel(self):
        return

    @wheel.setter
    def wheel(self, wheel):
        self.__wheels.append(wheel)

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, engine):
        self.__engine = engine

    def specification(self):
        print("=" * 30)
        print("Car Company: ", self.__company)
        print("Body: ", self.__body.shape)
        print("Engine: ", self.__engine.horsepower)
        print("Tire Size: ", self.__wheels[0].size)


class Director:
    __builder = None

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder):
        self.__builder = builder

    # The algorithm for assembling a car
    def get_car(self):
        car = Car(self.__builder.company)

        # First goes the body
        body = self.__builder.get_body()
        car.body = body

        # Then engine
        engine = self.__builder.get_engine()
        car.engine = engine

        # And four wheels
        i = 0
        while i < 4:
            wheel = self.__builder.get_wheels()
            car.wheel = wheel
            i += 1

        return car
