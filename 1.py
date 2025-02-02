'''
Class and Object
•	1. Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.
'''

class Employee:
    def __init__(self, name, id, department):
        self.name=name
        self.id=id
        self.department=department
    def display(self):
        print(f'Name:{self.name}\nID:{self.id}\nDepartment:{self.department}')

# assigning statistically
emp1 = Employee('Tharun',100,'CSE')
emp1.display()

# assigning dynamically
emp2 = Employee(input('Enter Name: '),int(input('Enter ID: ')),input('Enter Department: '))
emp2.display()


    