from __future__ import annotations

from abc import ABC, abstractmethod


class Observable(ABC):
    """
    The Observable interface declares a set of methods for managing observers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the observable.
        """
        raise NotImplementedError

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        raise NotImplementedError

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        raise NotImplementedError


class Observer(ABC):
    """
    The Observer interface declares the update method, used by observables.
    """

    @abstractmethod
    def update(self, observable: Observable) -> None:
        """
        Receive update from observable.
        """
        raise NotImplementedError
