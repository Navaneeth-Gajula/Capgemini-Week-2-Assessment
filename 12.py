'''
Polymorphism
•	12. Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently.
'''

class Payment:
    def process_payment(self):
        print('Processing Payment\n')

class CreditCardPayment(Payment):
    def process_payment(self):
        print('Processing Credit Card Payment\n')

class PayPalPayment(Payment):
    def process_payment(self):
        print('Processing PayPal Payment\n')

class BitcoinPayment(Payment):
    def process_payment(self):
        print('Processing Bitcoin Payment\n')

payment = Payment()
payment.process_payment()


credit_card_payment = CreditCardPayment()
credit_card_payment.process_payment()

paypal_payment = PayPalPayment()
paypal_payment.process_payment()

bitcoin_payment = BitcoinPayment()
bitcoin_payment.process_payment()