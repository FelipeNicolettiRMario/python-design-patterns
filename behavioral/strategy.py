from abc import ABC, abstractmethod

class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, weight: float) -> float:
        pass

class RegularShipping(ShippingStrategy):
    def calculate(self, weight: float) -> float:
        return weight * 0.25

class ExpressShipping(ShippingStrategy):
    def calculate(self, weight: float) -> float:
        return weight * 0.5

class AirFreightShipping(ShippingStrategy):
    def calculate(self, weight: float) -> float:
        return weight * 0.75

class ShippingCost:
    def __init__(self, strategy: ShippingStrategy):
        self._strategy = strategy

    def quote(self, weight: float) -> float:
        return self._strategy.calculate(weight)

    def set_strategy(self, strategy: ShippingStrategy):
        self._strategy = strategy

weight = 10 

regular = ShippingCost(RegularShipping())
print(f"Regular Shipping Cost: ${regular.quote(weight)}")

regular.set_strategy(ExpressShipping())
print(f"Express Shipping Cost: ${regular.quote(weight)}")

regular.set_strategy(AirFreightShipping())
print(f"Air Freight Shipping Cost: ${regular.quote(weight)}")
