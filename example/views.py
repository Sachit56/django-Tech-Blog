# example/views.py
# from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import TaskForm

def index(request):
    form=TaskForm()
    
    return render(request,'example/index.html',{
        'form':form
    })
    
    