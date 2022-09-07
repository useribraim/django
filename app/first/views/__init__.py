from app_api.models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
# from first.forms import StudentForm, ContactForm
import docx
import nltk

from .documents import *
from .sentences import *
from .clauses import *
from .syntaxemes import *
from .wordforms import *
from .upload import *
from .example import *
