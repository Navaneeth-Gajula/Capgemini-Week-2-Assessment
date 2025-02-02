'''
Polymorphism
•	11. Create a class `Logger` with a method `log(message)`. Implement method overloading to log different message types (`error`, `warning`, `info`).
'''

class Logger:
    def log(self, message):
        print(f'Log: {message}\n')

    def log(self, message, type):
        print(f'{type}: {message}\n')

log = Logger()
try:
    log.log('Error Message')
except TypeError:
    print('TypeError: log() missing 1 required positional argument: \'type\'')


log.log('Error Message','Error')
log.log('Warning Message','Warning')
log.log('Info Message','Info')
