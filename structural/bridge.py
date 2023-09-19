from abc import ABC, abstractmethod

class Engine(ABC):

    @abstractmethod
    def init(self):
        pass

class V8(Engine):

    def init(self):
        print("V8 Are running")

class V6(Engine):

    def init(self):
        print("V6 Are running")      

class Electrical(Engine):

    def init(self):
        print("Electrical engine is running")    

class Car(ABC):

    @property
    @abstractmethod
    def engine(self) -> Engine:
        pass

    @abstractmethod
    def start(self):
        pass


class BaseCar(Car):
    def __init__(self, engine: Engine) -> None:
        self._engine = engine

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, engine: Engine):
        self._engine = engine

    def start(self):
        pass  # Lógica comum de inicialização aqui

class TeslaModelS(BaseCar):
    def start(self):
        print("Tesla is running...")
        self.engine.init()

class DodgeCharger(BaseCar):
    def start(self):
        print("Dodge Charger is running...")
        self.engine.init()

if __name__ == "__main__":

    dodge = DodgeCharger(V8())
    dodge.start()

    print("---------------------------")

    dodge.engine = V6()
    dodge.start()

    print("---------------------------")

    tesla = TeslaModelS(Electrical())
    tesla.start()