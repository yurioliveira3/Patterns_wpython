from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits

#Memento interface 
class Memento(ABC):

    @abstractmethod
    def get_atual_state(self) -> str:
        pass

    @abstractmethod
    def set_atual_state(self) -> str:
        pass


#Concrete memento
class ConcreteMemento(Memento):
    def __init__(self, state, error, accuracy) -> None:
        self.state = state
        self.date = str(datetime.now())[:19]
        self.error = error
        self.accuracy = accuracy

    def get_state(self) -> str:
        #The Originator uses this method when restoring its state.
        return self.state

    def get_perform(self) -> str:
        #The rest of the methods are used by the Caretaker to display metadata.
        return f"NN: {state}, accuracy: {self.error}, error: {self.accuracy}, created: {self.date}"

    def get_date(self) -> str:
        return self.date

class Caretaker():
    """
    The Caretaker doesn't depend on the Concrete Memento class. Therefore, it
    doesn't have access to the originator's state, stored inside the memento. It
    works with all mementos via the base Memento interface.
    """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())
