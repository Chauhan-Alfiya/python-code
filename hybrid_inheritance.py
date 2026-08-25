class Animal:
    def eat(self):
        print("eating")

class Dog(Animal):
    def bark(self):
        print("bow wow")

class fish(Animal):
    def swin(self):
        print("swimming")

class Cat(Dog,fish):
    pass

cat = Cat()
cat.eat()
cat.bark()
cat.swin()