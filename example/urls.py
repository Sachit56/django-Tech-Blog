# example/urls.py
from django.urls import path

from example.views import index

app_name='example'
urlpatterns = [
    path('', index,name='home'),
]