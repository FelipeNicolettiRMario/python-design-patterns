class Target:

    def request(self):
        return "I work just fine"

class Adaptee:

    def specifc_request(self):
        return "REGNARTS OLLEH"
    
class Adapter(Target, Adaptee):

    def __init__(self) -> None:
        super().__init__()

    def request(self):
        return self.specifc_request()[::-1]
    
def client_code(target: Target):
    return target.request()

if __name__ == "__main__":

    target = Target()
    print(client_code(target))

    adapter = Adapter()
    print(client_code(adapter))
