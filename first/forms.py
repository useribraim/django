from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Document, Sentence, Clause





class StudentForm(forms.Form):
    firstname = forms.CharField(label="First name",max_length=50)  
    lastname  = forms.CharField(label="Last name", max_length = 10)  
    email     = forms.EmailField(label="Enter Email")  
    file      = forms.FileField() 

