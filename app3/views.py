from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def first(request):
    return HttpResponse('this is the first fuction')

def second(request):
    return HttpResponse("<h1>This is the second function</h1>")


def third(request):
    return HttpResponse("<h1> This is the third function <h1>")

def forth(request):
    return HttpResponse("<h2>This is the forth function <h2>")

def fifth(request):
    return HttpResponse("<h2> This is the fifth function </h2>")