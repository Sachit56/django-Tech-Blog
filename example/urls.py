# example/urls.py
from django.urls import path

from example.views import index,UpdateView,DeleteView

app_name='example'
urlpatterns = [
    path('', index,name='home'),
    path('update/<int:pk>',UpdateView,name='update'),
    path('delete/<int:pk>',DeleteView,name='delete')
]