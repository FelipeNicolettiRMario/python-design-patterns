from abc import ABC, abstractclassmethod

class Terminator(ABC):

    @abstractclassmethod
    def terminate(self):
        """Will terminate"""

    def clone(self):
        """Will clone the terminator"""

class ConcreteTerminator(Terminator):

    def __init__(self, model) -> None:
        self.model = model
        super().__init__()

    def terminate(self):
        print(f"I am the terminator {self.model} and I will terminate you!")

    def clone(self):
        return ConcreteTerminator(model=self.model)
    
def make_terminator(terminator: Terminator):
    """This example shows how you can implemente the Propotype pattern
        generating 
    """
    terminator.terminate()

    terminator_2 = terminator.clone()
    terminator_2.terminate()

    terminator_3 = terminator_2.clone() 
    terminator_3.terminate()

    print(terminator, terminator_2, terminator_3)


if __name__ == "__main__":

    make_terminator(ConcreteTerminator("T800"))