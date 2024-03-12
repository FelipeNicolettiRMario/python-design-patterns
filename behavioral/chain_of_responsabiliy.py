from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle_request(self, amount):
        pass

class TeamLeader(Handler):
    def handle_request(self, amount):
        if amount <= 1000:
            print(f"TeamLeader approved the expense {amount}.")
        elif self._successor is not None:
            self._successor.handle_request(amount)

class DepartmentManager(Handler):
    def handle_request(self, amount):
        if amount <= 5000:
            print(f"DepartmentManager approved the expense {amount}.")
        elif self._successor is not None:
            self._successor.handle_request(amount)

class GeneralManager(Handler):
    def handle_request(self, amount):
        if amount <= 10000:
            print(f"GeneralManager approved the expense {amount}.")
        else:
            print("Expense required an executive meeting for approval.")

if __name__ == "__main__":
    team_leader = TeamLeader()
    department_manager = DepartmentManager(team_leader)
    general_manager = GeneralManager(department_manager)

    general_manager.handle_request(500)
    general_manager.handle_request(1500)
    general_manager.handle_request(6500)
    general_manager.handle_request(15000)
