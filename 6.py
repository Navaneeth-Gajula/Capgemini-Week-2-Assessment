'''
Inheritance (Multiple, Multi-Level)
•	7. Create a multi-level class structure with `Person` → `Employee` → `Manager`, where `Manager` has an additional method `approve_leave()`.
'''

class Person:
    def __init__(self, name, age, blood_group):
        print('Person Details\n')
        self.name=name
        self.age=age
        self.blood_group=blood_group

    def display(self):
        print(f'Person name: {self.name}\nPerson Age: {self.age}\nPerson Blood Group: {self.blood_group}\n')

    def work(self):
        print('Person is working\n')

class Employee(Person):
    def __init__(self, name, age, blood_group, id, department):
        self.name=name
        self.age=age
        self.blood_group=blood_group
        self.id=id
        self.department=department

    def display(self):
        print(f'Employee ID: {self.id}\nEmployee Department: {self.department}\n')
        return super().display()
    
    def work(self):
        print('Employee is working\n')


class Manager(Employee):
    def __init__(self, name, age, blood_group, id, department, team, managername):
        self.name=name
        self.age=age
        self.blood_group=blood_group
        self.id=id
        self.department=department
        self.team=team
        self.managername=managername

    def display(self):
        print(f'Manager Team: {self.team}\n')
        return super().display()
    
    def approve_leave(self):
        print(f'Leave Approved to {self.name} by manager {self.managername}\n')

    def work(self):
        print(f'Manager {self.managername} is working\n')

person1 = Person('Tharun',20,'O+')
person1.display()
person1.work()

emp1 = Employee('Tharun',20,'O+',100,'CSE') 
emp1.display()
emp1.work()

manager1 = Manager('Tharun',20,'O+',100,'CSE','CSE Team','bheem')
manager1.display()
manager1.approve_leave()
manager1.work()