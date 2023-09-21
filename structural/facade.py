class Engine:

    def start(self):    
        print("Engine started!")

class Reactor:

    def start(self):
        print("Reactor started!")

class GravitationalEngine:

    def start(self):
        print("Gravitational engine started!")

class Spaceship:

    def __init__(self, engine: Engine, reactor: Reactor, gv_engine: GravitationalEngine) -> None:
        self.engine = engine
        self.reactor = reactor
        self.gv_engine = gv_engine

    def start(self):

        print("Initing proccess to start spaceship...")
        self.reactor.start()
        self.gv_engine.start()
        self.engine.start()
        print("Spaceship started!")

if __name__ == "__main__":

    ship = Spaceship(
        Engine(),
        Reactor(),
        GravitationalEngine()
    )

    ship.start()
