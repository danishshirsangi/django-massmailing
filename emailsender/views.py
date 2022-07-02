from audioop import reverse
import os
from statistics import mode
from django.shortcuts import redirect, render
from validate_email import validate_email
from django.core.mail import send_mail
from maildispatch.settings import EMAIL_HOST_USER as from_user_default


from emailsender.models import EmailCsvModel
from .forms import EmailFormView
import csv
# Create your views here.
d = {'valid': [],'invalid': []}

def home_view_main(request):
    return render(request, 'index2.html')

def home_view(request):
    context = {}
    global d
    d['valid'].clear()
    d['invalid'].clear()
    if request.method == "POST" and request.FILES:
        nm = request.POST.get('filename')
        fc = request.FILES.get('filecs')
        obj = EmailCsvModel(name=nm, file_hold=fc)
        obj.save()
        emailValidiate(obj)
        s = EmailCsvModel.objects.get(file_hold=obj.file_hold)
        print(s)
        s.delete()
    context['valid'] = d['valid']
    context['invalid'] = d['invalid']
    return render(request, 'upload.html',context)

def with_body(request):
    if request.method == "POST":
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        send_mail(sub,msg,from_user_default,[x for x in d['valid']],fail_silently=False,)
        return redirect('/')
    
    return render(request, 'send.html',{"def_mail":from_user_default})


def send_again(request):
    return redirect(request.META['HTTP_REFERER'])

def check_mail(row):
    global d
    if validate_email(row[0]):
        d['valid'].append(row[0])
    else:
        d['invalid'].append(row[0])

def emailValidiate(obj):
    file = obj.file_hold.open(mode='r')
    fileObj = csv.reader(file)
    for row in fileObj:
        check_mail(row)


def about_view(request):
    return render(request, 'about.html')