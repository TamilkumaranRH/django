from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def n1(request):
    return HttpResponse("<p> this is new text </p>")
def n2(t):
    return render(t,'design.html')