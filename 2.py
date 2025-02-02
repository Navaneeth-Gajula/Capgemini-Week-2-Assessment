'''
Class and Object
•	2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.
'''
#overdr
class BankAccount:
    def __init__(self):
        print('Welcome to Bank Account\n')
        self.balance=0
    
    def deposit(self, money):
        self.balance+=money
        print(f'Amount Deposited is: {money} \nThe total balance is: {self.balance}\n')

    def withdraw(self, money):
        if self.balance>=money:
            self.balance-=money
            print(f'The withdrawn amount is: {money}\nThe Total available balance is: {self.balance}\n')
        else:
            print(f'Insufficient Balance. Current balance is: {self.balance}. \nPlease enter amount Less than or equal to the balance\n')


bankacc = BankAccount()
bankacc.deposit(100)
bankacc.deposit(200)
bankacc.withdraw(1000)
bankacc.withdraw(150)
bankacc.withdraw(150)
bankacc.deposit(int(input('Enter amount to deposit: ')))
bankacc.withdraw(int(input('Enter amount to withdraw: ')))