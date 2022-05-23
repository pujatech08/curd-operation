from dataclasses import field, fields
from tkinter import Widget
from django.core import validators
from django import forms
from .models import user

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=user
        fields={'name','password','email'}
        widgets = {
            'name' : forms.TextInput(attrs = {'class':'form-control col-md-6'}),
            'password': forms.PasswordInput(attrs = {'class':'form-control col-md-6'}),
            'email': forms.EmailInput(attrs = {'class':'form-control col-md-6'}),     
        }
