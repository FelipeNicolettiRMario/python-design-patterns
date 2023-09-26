from abc import ABC, ABCMeta, abstractmethod

class Subject(ABC):

    @abstractmethod
    def request(self) -> None:
        pass

class ConcreteSubject(Subject):

    def request(self) -> None:
        print("Request made...")

class Proxy(Subject):

    def __init__(self, user_role: str) -> None:
        self.user_role = user_role
        self._real_subject = ConcreteSubject()

    def _has_permission(self) -> bool:

        if self.user_role.lower() == "operator":
            return False
        
        if self.user_role.lower() == "admin":
            return True
        
    def request(self) -> None:
        
        if self._has_permission():
            return self._real_subject.request()
        
if __name__ == "__main__":

    proxy = Proxy("admin")
    proxy.request()