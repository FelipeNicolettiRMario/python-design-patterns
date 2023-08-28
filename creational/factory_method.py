from abc import ABC, abstractclassmethod



class Product(ABC):

    @abstractclassmethod
    def do_stuff(self):
        """Doing some stuff..."""

class Creator(ABC):

    @abstractclassmethod
    def create(self) -> Product:
        """Creates the products"""

class Product1(Product):

    def do_stuff(self):
        print("Product1 doing stuff...")

class Creator1(Creator):

    def create(self):
        return Product1()
    
class Product2(Product):

    def do_stuff(self):
        print("Product2 doing stuff...")

class Creator2(Creator):

    def create(self):
        return Product2()
    
def init_process(creator: Creator):
    """This methods expect to receive an interface of a creator, you dont need to pass details about
        the implementation of the class.
    """


    print(f"I'm agnostic to implementantion, i'm running the class {creator.__class__.__name__}")

    product = creator.create()

    product.do_stuff()

if __name__ == "__main__":

    init_process(Creator2())