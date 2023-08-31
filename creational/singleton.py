class SingletonMeta(type):

    _instance = {}

    def __call__(cls, *args, **kwargs) -> None:
        
        if not cls._instance:

            instance = super().__call__(*args, **kwargs) 
            cls._instance[cls] = instance

        return cls._instance[cls]

class Singleton(metaclass=SingletonMeta):
    pass

if __name__ == "__main__":

    """In this example a singleton with a multiple instances implementation is build"""

    s1 = Singleton()
    s2 = Singleton()

    print(s1 == s2)


