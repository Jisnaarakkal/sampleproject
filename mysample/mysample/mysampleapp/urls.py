
from django.urls import path

from mysampleapp import views

urlpatterns = [

    path('', views.index,name='index'),
    path('result/',views.result,name='result'),
    ]