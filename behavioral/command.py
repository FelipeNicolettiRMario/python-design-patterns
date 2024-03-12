from abc import ABC, abstractmethod
import copy

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state

class Stock:

    def __init__(self) -> None:
        self.items = []
        self._memento = None

    def create_memento(self):
        return Memento(copy.deepcopy(self.items))

    def set_memento(self, memento):
        self.items = memento.get_state()

class AddItemsToStockCommand(Command):

    def __init__(self, stock) -> None:
        self.stock: Stock = stock
        self.previous_memento = None
        self.future_memento = None

    def execute(self, item):
        self.previous_memento = self.stock.create_memento()
        self.stock.items.append(item)
        self.future_memento = self.stock.create_memento()

    def undo(self):
        if self.previous_memento:
            self.stock.set_memento(self.previous_memento)

    def redo(self):
        if self.future_memento:
            self.stock.set_memento(self.future_memento)

if __name__ == "__main__":

    stock = Stock()

    add_to_stock_command = AddItemsToStockCommand(stock)

    add_to_stock_command.execute(10)

    print("Adding items to stock...")
    print("Items in stock:", stock.items)

    add_to_stock_command.undo()
    print("Undoing operation...")
    print("Items in stock:", stock.items)

    add_to_stock_command.redo()
    print("Redoing operation...")
    print("Items in stock:", stock.items)
