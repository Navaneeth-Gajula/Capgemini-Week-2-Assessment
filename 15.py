'''
Polymorphism
•	15. Write an example where `Operator Overloading` is used to concatenate two `Book` objects, treating them as a series.
'''

class Book:
    def __init__(self, title, author, isbn):
        self.title=title
        self.author=author
        self.isbn=isbn

    def __add__(self, args):
        return f'{self.title} by {self.author} with {self.isbn} and {args.title} by {args.author} with {self.isbn}'
    

book1 = Book('Harry Potter','J.K.Rowling',128546)
book2 = Book('The Alchemist','Paulo Coelho',128547)
print(book1+book2)

book3 = Book(input('Enter Title: '),input('Enter Author: '),int(input('Enter ISBN: ')))
book4 = Book(input('Enter Title: '),input('Enter Author: '),int(input('Enter ISBN: ')))
print(book3+book4)