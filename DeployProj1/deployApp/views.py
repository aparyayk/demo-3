from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    s1='<h1>Hello World!!Deployment</h1><br>'
    s2='<h2>Hello World!!Deployment</h2>'
    return HttpResponse(s1+s2)