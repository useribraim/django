from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect

def foo(request):
    print(request.POST)
    return render(request,"first/other/example.html")  

