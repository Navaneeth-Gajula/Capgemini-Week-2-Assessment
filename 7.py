'''
Inheritance (Multiple, Multi-Level)
•	8. Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.
'''

class Animal:
    def __init__(self, name):
        self.name=name

    def speak(self):
        print('Animal speaks\n')

class Dog(Animal):
    def __init__(self, name, breed):
        self.name=name
        self.breed=breed

    def speak(self):
        print(f'Dog {self.breed} Barks\n')

class Cat(Animal):
    def __init__(self, name, breed):
        self.name=name
        self.breed=breed

    def speak(self):
        print(f'Cat {self.breed} Meows\n')

animal = Animal('Animal')
animal.speak()

dog = Dog('Dog','Labrador')
dog.speak()

cat = Cat('Cat','Persian')
cat.speak()