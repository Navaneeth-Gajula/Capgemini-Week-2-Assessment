'''
Interface (Using Abstract Base Classes - ABC)
•	20. Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, and it is implemented by `GoogleAuth` and `FacebookAuth` classes.
'''

from abc import ABC, abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

class GoogleAuth(UserAuthentication):
    def login(self):
        print('Google login successful')

    def logout(self):
        print('Google logout successful')

class FacebookAuth(UserAuthentication):
    def login(self):
        print('Facebook login successful')

    def logout(self):
        print('Facebook logout successful')


google = GoogleAuth()
google.login()
google.logout()

facebook = FacebookAuth()
facebook.login()
facebook.logout()

