from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Document, Sentence, Clause





class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    file      = forms.FileField() 

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(max_length = 10)  

