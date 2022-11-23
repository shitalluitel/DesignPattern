from random import randrange
from typing import List

from DesignPattern.Behavioral.observer.observer import Observable, Observer


class ConcreteSubject(Observable):
    """
    The Observable owns some important state and notifies observers when the state
    changes.
    """

    _state: int = None
    """
    For the sake of simplicity, the Observable's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """

    @property
    def state(self):
        return self._state

    def attach(self, observer: Observer) -> None:
        print("Observable: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Observable: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Observable can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nObservable: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Observable: My state has just changed to: {self._state}")
        self.notify()


"""
Concrete Observers react to the updates issued by the Observable they had been
attached to.
"""


class ConcreteObserverA(Observer):
    def update(self, observable: Observable) -> None:
        if observable.state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, observable: Observable) -> None:
        if observable.state == 0 or observable.state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    observable = ConcreteSubject()

    # Attach concrete observer A within observable
    observer_a = ConcreteObserverA()
    observable.attach(observer_a)

    # Attach concrete observer B within observable
    observer_b = ConcreteObserverB()
    observable.attach(observer_b)

    # 1st change of state
    observable.some_business_logic()

    # 2nd change of state
    observable.some_business_logic()

    # Remove concrete observer A within observable
    observable.detach(observer_a)

    # 3rd change of state
    observable.some_business_logic()
