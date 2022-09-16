from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return  render(request,"index.html")

def result(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y
    sub=x-y
    mult=x*y
    div=x/y
    return  render(request,"result.html",{'addres':add,'subres':sub,'mulres':mult,'divres':div})