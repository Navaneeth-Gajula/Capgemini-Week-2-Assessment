'''
Interface (Using Abstract Base Classes - ABC)
•	16. Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.
'''

from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(IShape):
    def calculate_area(self, length, breadth):
        return length*breadth
    
class Circle(IShape):
    def calculate_area(self, radius):
        return 3.14*radius*radius
    
rectangle = Rectangle()
print('Area of Rectangle:',rectangle.calculate_area(5,10))

circle = Circle()
print('Area of Circle:',circle.calculate_area(5))


