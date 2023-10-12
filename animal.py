class Animal:
    def __init__(self, name, eat, drink):
        self.name = name
        self.eat = eat
        self.drink = drink

    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")

class Frog(Animal):
    def __init__(self, name, jump):
        self.name = name
        self.jump = jump

    def jump(self):
        print(f"{self.name} is jumping")
        
