'''
Interface (Using Abstract Base Classes - ABC)
•	17. Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.
'''

from abc import ABC, abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print('Inserting data into SQL Database')

    def update(self):
        print('Updating data in SQL Database')

    def delete(self):
        print('Deleting data from SQL Database')

class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print('Inserting data into NoSQL Database')

    def update(self):
        print('Updating data in NoSQL Database')

    def delete(self):
        print('Deleting data from NoSQL Database')

sql = SQLDatabase()
sql.insert()
sql.update()
sql.delete()

nosql = NoSQLDatabase()
nosql.insert()
nosql.update()
nosql.delete()
