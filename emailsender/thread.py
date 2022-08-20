import threading
from tkinter import E
from validate_email import validate_email
from django.core.mail import send_mail,EmailMessage

class SendMailClass(threading.Thread):
    def __init__(self, mail):
        threading.Thread.__init__(self)
        self.mail = mail

    def run(self):
        print("Sending Mails",self.mail)
        try:
            print(self.mail.send())
        except Exception as e:
            print(e)
    
class GatherEmails(threading.Thread):
    def __init__(self, file):
        threading.Thread.__init__(self)
        self.fileobj = file
        self.dic = {'valid': [],'invalid': []}


    def _check_mail(self, row):
        try:
            if validate_email(row[0]):
                self.dic['valid'].append(row[0])
            else:
                self.dic['invalid'].append(row[0])
        except Exception as e:
            print(e)

    def get_emails(self):
        for row in self.fileobj:
            self._check_mail(row)
        return self.dic