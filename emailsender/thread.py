import threading
from validate_email import validate_email
from django.core.mail import send_mail

class SendMailClass(threading.Thread):
    def __init__(self, sub, msg, sender_mail, mails_list):
        threading.Thread.__init__(self)
        self.message = msg
        self.subject = sub
        self.sender = sender_mail
        self.mails_list = mails_list
        try:
            print("Sending Mails")
            print(self.mails_list)
            print(send_mail(self.subject, self.message, self.sender, self.mails_list, fail_silently=False))
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