from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

class TemperatureSensor(Subject):
    def __init__(self):
        super().__init__()
        self._temperature = 0

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, temperature):
        self._temperature = temperature
        self.notify()

class TemperatureDisplay(Observer):
    def update(self, temperature):
        print(f"Temperature Display: Temperature has changed to {temperature}°C")

sensor = TemperatureSensor()
display1 = TemperatureDisplay()
display2 = TemperatureDisplay()

sensor.attach(display1)
sensor.attach(display2)

sensor.set_temperature(25)
sensor.detach(display1)
sensor.set_temperature(30)