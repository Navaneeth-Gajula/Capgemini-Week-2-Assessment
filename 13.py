'''
Polymorphism
•	13. Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.

'''

class Shape:
    def area(self):
        pass

class Square(Shape):
    def area(self, side):
        return side*side
    
class Triangle(Shape):
    def area(self, base, height):
        return 0.5*base*height
    
shape = Shape()
print('Area of Shape:',shape.area())

square = Square()
print('Area of Square:',square.area(5))

triangle = Triangle()
print('Area of Triangle:',triangle.area(5,15))