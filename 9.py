'''
Inheritance (Multiple, Multi-Level) 
•	9. Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `Airplane`. Handle potential conflicts in the `move()` method.
'''

class Car:
    def __init__(self, name, color, brand, model):
        self.name = name
        self.color = color
        self.brand = brand
        self.model = model

    def start(self):
        print(f'{self.name} Started\n')

    def move(self):
        print(f'{self.name} is moving on the road\n')

class Airplane:
    def __init__(self, name, color, brand, model):
        self.name = name
        self.color = color
        self.brand = brand
        self.model = model

    def fly(self):
        print(f'{self.name} is flying in the sky\n')

    def move(self):
        print(f'{self.name} is moving in the sky\n')

class FlyingCar(Car, Airplane):
    def __init__(self, name, color, brand, model, fuel):
        self.name = name
        self.color = color
        self.brand = brand
        self.model = model
        self.fuel = fuel

    def start(self):
        print(f'{self.name} Started\n')

    def move(self):
        print(f'{self.name} is moving on the road and in the sky\n')

car = Car('Car', 'Red', 'Toyota', 'Corolla')
car.start()
car.move()

airplane = Airplane('Airplane', 'White', 'Boeing', '747')
airplane.fly()
airplane.move()

flyingcar = FlyingCar('Flying Car', 'Black', 'Tesla', 'Model S', 'Electric')
flyingcar.start()
flyingcar.move()
flyingcar.fly()
