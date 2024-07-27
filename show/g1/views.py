from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def frame(t):
    return HttpResponse("<p>this a application</p>")
def page1(r):
    return render(r,'news.html')