import asyncio
from django.shortcuts import redirect, render

import string
import random

from maildispatch.settings import EMAIL_HOST_USER as from_user_default

from .thread import GatherEmails, SendMailClass

from django.core.mail import EmailMessage


from emailsender.models import EmailCsvModel
from .forms import EmailFormView
import csv
# Create your views here.

d = {'valid':[],'invalid':[]}
def home_view_main(request):
    return render(request, 'index2.html')

def home_view(request):
    context = {}
    global d
    d['valid'].clear()
    d['invalid'].clear()
    if request.method == "POST" and request.FILES:
        res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=15))
        fc = request.FILES.get('filecs')
        obj = EmailCsvModel(name=res, file_hold=fc)
        obj.save()
        mails = emailValidiate(obj)
        d['valid'] = mails['valid']
        # print(d['valid'])
        s = EmailCsvModel.objects.get(file_hold=obj.file_hold)
        # print(s)
        context['valid'] = mails['valid']
        context['invalid'] = mails['invalid']
    return render(request, 'upload.html',context)

def with_body(request):
    global d
    if request.method == "POST":
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        mails_list = d['valid']
        print(mails_list)
        email = EmailMessage(sub, msg,from_user_default, mails_list)
        SendMailClass(email).start()
        return redirect('/')
    
    return render(request, 'send.html',{"def_mail":from_user_default})


def send_again(request):
    return redirect(request.META['HTTP_REFERER'])


def emailValidiate(obj):
    file = obj.file_hold.open(mode='r')
    fileObj = csv.reader(file)
    res = GatherEmails(fileObj).get_emails()
    return res

def about_view(request):
    return render(request, 'about.html')