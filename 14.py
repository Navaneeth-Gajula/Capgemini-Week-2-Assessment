'''
Polymorphism
•	14. Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`.
'''

class Notification:
    def send(self):
        pass

class EmailNotification(Notification):
    def send(self):
        print('Sending Email Notification\n')

class SMSNotification(Notification):
    def send(self):
        print('Sending SMS Notification\n')


notification = Notification()
notification.send()

email_notification = EmailNotification()
email_notification.send()

sms_notification = SMSNotification()
sms_notification.send()

