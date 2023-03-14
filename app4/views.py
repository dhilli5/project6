from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_app4(request):
    return HttpResponse("this is the first app4 function")

def second_app4(request):
    return HttpResponse("<h1> This is the app4 second function</h1>")