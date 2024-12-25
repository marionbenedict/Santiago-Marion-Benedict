from abc import ABC, abstractmethod

class NinjaTurtle(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

class Leonardo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self._real_name = real_name
        self._alias = alias

    @property
    def name(self):
        return self._alias


class Michelangelo(NinjaTurtle):
    def __init__(self, real_name, alias):
        self._real_name = real_name
        self._alias = alias

    @property
    def name(self):
        return self._alias


class Donatello(NinjaTurtle):
    def __init__(self, real_name, alias):
        self._real_name = real_name
        self._alias = alias

    @property
    def name(self):
        return self._alias


class Raphael(NinjaTurtle):
    def __init__(self, real_name, alias):
        self._real_name = real_name
        self._alias = alias

    @property
    def name(self):
        return self._alias


def main():
    # Create instances of the turtles
    leo = Leonardo("Leonardo", "Leo")
    mikey = Michelangelo("Michelangelo", "Mikey")  # Adjusted alias for consistency
    don = Donatello("Donatello", "Don")
    raph = Raphael("Raphael", "Raph")

    # Print their aliases
    print(leo.name)
    print(mikey.name)
    print(don.name)
    print(raph.name)


if __name__ == "__main__":
    main()