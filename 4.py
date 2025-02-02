'''
Class and Object
•	4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details.
'''

class Student:
    def __init__(self, name, roll_number):
        print('Student Details\n')
        self.name=name
        self.roll_number=roll_number

    def show(self):
        print(f'Name of Student:{self.name}\nRoll NUmber of Student: {self.roll_number}\n')

stud1 = Student('Tharun',14)
stud1.show()

stud2 = Student(input('Enter Name: '),int(input('Enter Roll Number: ')))
stud2.show()