'''
Class and Object
•	3. You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to display book details.
'''

class Book:
    def __init__(self, title, author, isbn):
        print('Library Management System\n')
        self.title=title
        self.author=author
        self.isbn=isbn

    def display(self):
        print(f'Tile of book: {self.title}\nAuthor of the Book: {self.author}\nISBN of Book: {self.isbn}\n')

book1 = Book('Harry Potter','J.K.Rowling',128546)
book1.display()

book2 = Book(input('Enter Title: '),input('Enter Author: '),int(input('Enter ISBN: ')))
book2.display()
