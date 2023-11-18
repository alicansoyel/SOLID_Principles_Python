from abc import ABC, abstractmethod

class Eater(ABC):
    @abstractmethod
    def eat(self):
        pass

class Worker(ABC):
    @abstractmethod
    def work(self, document):
        pass

class Swim(ABC):
    @abstractmethod
    def swim(self, document):
        pass


class Human(Eater,Worker,Swim):
    def eat(self):
        print("Human is eating...")
    def work(self):
        print("Human is working...")
    def swim(self):
        print("Human is swimming...")


class Fish(Eater,Swim):
    def eat(self):
        print("Fish is eating...")
    def swim(self):
        print("Fish is swimming...")

 

if __name__ == '__main__':
    human = Human()
    human.work()
    human.eat()
    human.swim()

    fish = Fish()
    fish.eat()  
    fish.swim() 
