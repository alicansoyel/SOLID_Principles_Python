from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass

class Dove(Bird):
    def fly(self):
        print("Dove flying...")

    def eat(self):
        print("Dove eating...")


class Pigeon(Bird):
    def fly(self):
        print("Pigeon flying...")

    def eat(self):
        print("Pigeon eating...")

class SomersaultingPigeon(Pigeon):
    def somersault(self):
        print("Pigeon somersaulting...")


if __name__ == '__main__':
    #Pigeon
    pigeon = SomersaultingPigeon()
    pigeon.eat()
    pigeon.fly()
    pigeon.somersault()
    
    #Dove
    dove = Dove()
    dove.eat()
    dove.fly()
    