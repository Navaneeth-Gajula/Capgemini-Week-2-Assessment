'''
Interface (Using Abstract Base Classes - ABC)
•	18. Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. Create a `BasicCalculator` class that implements these methods.
'''

from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass

    @abstractmethod
    def subtract(self, a, b):
        pass

    @abstractmethod
    def multiply(self, a, b):
        pass

    @abstractmethod
    def divide(self, a, b):
        pass

class BasicCalculator(ICalculator):
    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b
    
calculator = BasicCalculator()
print('Addition:',calculator.add(5,10))
print('Subtraction:',calculator.subtract(10,5))
print('Multiplication:',calculator.multiply(5,10))
print('Division:',calculator.divide(10,5))

