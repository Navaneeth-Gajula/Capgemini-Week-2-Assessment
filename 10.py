'''
Inheritance (Multiple, Multi-Level)
•	10. Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`. Demonstrate method overriding and attribute reuse.
'''

class Electronics:
    def __init__(self, name, brand, model):
        self.name=name
        self.brand=brand
        self.model=model

    def display(self):
        print(f'Name: {self.name}\nBrand: {self.brand}\nModel: {self.model}\n')

class MobileDevice(Electronics):
    def __init__(self, name, brand, model, os):
        self.name=name
        self.brand=brand
        self.model=model
        self.os=os

    def display(self):
        print(f'OS: {self.os}\n')
        return super().display()

    def call(self):
        print('Mobile Device is calling\n')

class SmartPhone(MobileDevice):
    def __init__(self, name, brand, model, os, camera):
        self.name=name
        self.brand=brand
        self.model=model
        self.os=os
        self.camera=camera

    def display(self):
        print(f'Camera: {self.camera}\n')
        return super().display()

    def call(self):
        print('SmartPhone is calling\n')

    def games(self):
        print('Playing games in SmartPhone\n')


electronics = Electronics('Electronics','Samsung','Galaxy')
electronics.display()

mobiledevice = MobileDevice('Mobile Device','Apple','iPhone','iOS')
mobiledevice.display()
mobiledevice.call()

smartphone = SmartPhone('SmartPhone','OnePlus','8T','Android','48MP')
smartphone.display()
smartphone.call()
smartphone.games()