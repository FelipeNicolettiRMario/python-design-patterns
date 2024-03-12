class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state
        print(f"Originator: Setting state to {self._state}")

    def save_to_memento(self):
        print("Originator: Saving to Memento.")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_state()
        print(f"Originator: State after restoring from Memento: {self._state}")

class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]

originator = Originator()
caretaker = Caretaker()

originator.set_state("State #1")
caretaker.add_memento(originator.save_to_memento())

originator.set_state("State #2")
caretaker.add_memento(originator.save_to_memento())

originator.set_state("State #3")
print("Current State:", originator._state)

originator.restore_from_memento(caretaker.get_memento(0))
