from django import forms
from .models import EmailCsvModel


class EmailFormView(forms.ModelForm):
    class Meta:
        model = EmailCsvModel
        fields = ['name', 'file_hold']
