from builder import JeepBuilder, NissanBuilder
from director import Director


class Handler:
    builders = [JeepBuilder, NissanBuilder]
    director = Director()
    cars = None

    def handle(self):
        for BuilderKlass in self.builders:
            self.director.builder = BuilderKlass()
            car = self.director.get_car()

            if not self.cars:
                self.cars = [car]
            else:
                self.cars.append(car)

    def display_specification(self):
        for car in self.cars:
            car.specification()


handler = Handler()
handler.handle()
handler.display_specification()
