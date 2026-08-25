class Animal:
    def eat(self):
        print("eating")

class Dog(Animal):
    def bark(self):
        print("bow wow")

class fish(Animal):
    def swin(self):
        print("swimming")

dog = Dog()
dog.eat()
dog.bark()

fish = fish()
fish.eat()
fish.swim()