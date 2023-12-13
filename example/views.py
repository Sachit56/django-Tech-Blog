# example/views.py
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render,redirect

def index(request):
    # return render(request,'example/index.html')
    return HttpResponse('Hello')
    