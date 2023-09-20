class Subordinate:

    def __init__(self, name: str, position: str):

        self.name = name
        self.position = position

    def __repr__(self) -> str:
        return f"<Subordinate {self.name} - position {self.position}>"

class Manager(Subordinate):

    def __init__(self, name: str, position: str):
        super().__init__(name, position)
        self._subordinates = set()

    @property
    def subordinates(self):
        return self._subordinates
    
    def add_subordinate(self, subordinate: Subordinate):
        self._subordinates.add(subordinate)

    def remove(self, subordinate: Subordinate):
        self._subordinates.discard(subordinate)

    def __repr__(self) -> str:
        return f"<Manager {self.name} - position {self.position}>"

if __name__ == "__main__":

    director = Manager(name="Jan Levinson", position="Director")

    hrbp = Subordinate(name="Toby Flanderson", position="HRBP")

    regional_manager = Manager(name="Michael Scott", position="Regional Manager")

    salesman_1 = Subordinate(name="Jim", position="Salesman")
    assistant_of_the_regional_manager = Subordinate(name="Dwight Schrute", position="Salesman")
    secretary = Subordinate(name="Pam", position="Secretary")
    intern = Subordinate(name="Luke Cooper", position="Intern")

    director.add_subordinate(hrbp)
    
    regional_manager.add_subordinate(salesman_1)
    regional_manager.add_subordinate(assistant_of_the_regional_manager)
    regional_manager.add_subordinate(secretary)
    regional_manager.add_subordinate(intern)

    director.add_subordinate(regional_manager)

    print(director)
    print(director.subordinates)
    print("---------------------------")

    print(regional_manager)
    print(regional_manager.subordinates)
    print("---------------------------")

    regional_manager.remove(intern)

    print(regional_manager)
    print(regional_manager.subordinates)
    print("---------------------------")
