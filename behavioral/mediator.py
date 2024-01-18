"""In this code, we will simulate a production line of an airplane,
    when one step of the production is completed, the quality sector must be warned the director
"""

from abc import ABC, abstractmethod

class IDirector(ABC):

    @abstractmethod
    def step_completed(self):
        pass

class Quality:

    def inspect(self):
        print("Inspecting...passed!")

class Director(IDirector):

    def __init__(self,quality: Quality) -> None:
        self.quality = Quality()

    def step_completed(self):
        self.quality.inspect()

class BodyShop:

    def __init__(self, quality_director: Director) -> None:
        self.quality_director = quality_director

    def _warn_quality(self):
        self.quality_director.step_completed()

    def funnel(self):
        print("Funneling...")
        self._warn_quality()

if __name__ == "__main__":

    q = Quality()
    qd = Director(q)
    bs = BodyShop(qd)

    bs.funnel()




