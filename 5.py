'''
Inheritance (Multiple, Multi-Level)
•	6. Implement a multi-level inheritance example where `Vehicle` is a base class, `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.
'''

class Vehicle:
    def __init__(self, name, color):
        print('All Specifications of Vehicle\n')
        self.name=name
        self.color=color

    def display(self):
        print(f'Vehicle Name: {self.name}\nVehicle Color: {self.color}\n')

class Car(Vehicle):
    def __init__(self,name,color,brand,model):
        self.name=name
        self.color=color
        self.brand=brand
        self.model=model

    def display(self):
        print(f'Car Brand: {self.brand}\nCar Model: {self.model}\n')
        return super().display()

    def start(self):
        print('Car Started\n')

class Bike(Vehicle):
    def __init__(self,name,color,brand,model):
        self.name=name
        self.color=color
        self.brand=brand
        self.model=model

    def display(self):
        print(f'Bike Brand: {self.brand}\nBike Model: {self.model}\n')
        return super().display()
    
    def start(self):
        print('Bike Started\n')

class ElectricCar(Car):
    def __init__(self, name, color, brand, model, battery_capacity):
        self.name=name
        self.color=color
        self.brand=brand
        self.model=model
        self.battery_capacity=battery_capacity

    def display(self):
        print(f'Battery Capacity: {self.battery_capacity}\n')
        return super().display()
    
    def start(self):
        print('Electric Car Started\n')


lorry = Vehicle('Lorry','White')
lorry.display()

car = Car('Car','Red','Audi','A6')
car.display()
car.start()

bike = Bike('Bike','Black','Royal Enfield','Classic 350')
bike.display()
bike.start()

el_Car = ElectricCar('Electric Car','Blue','Tesla','Model S',100)
el_Car.display()
el_Car.start()

