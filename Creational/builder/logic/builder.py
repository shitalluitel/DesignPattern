"""
Creates various parts of a vehicle.

This class is responsible for constructing all
the parts for a vehicle.
"""

import abc


class Builder(abc.ABC):
    company = None

    @abc.abstractmethod
    def get_wheels(self):
        raise NotImplemented

    @abc.abstractmethod
    def get_body(self):
        raise NotImplemented

    @abc.abstractmethod
    def get_engine(self):
        raise NotImplemented


class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


class JeepBuilder(Builder):
    company = 'Jeep'

    def get_wheels(self):
        wheel = Wheel()
        wheel.size = 10
        return wheel

    def get_body(self):
        body = Body()
        body.shape = 'HatchBack'
        return body

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 24
        return engine


class NissanBuilder(Builder):
    company = 'Nissan'

    def get_wheels(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel

    def get_body(self):
        body = Body()
        body.shape = 'SUV'
        return body

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 32
        return engine
