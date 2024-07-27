from django.shortcuts import render
from django.http import HttpResponse  
from django.views import View  

# Create your views here.
from .models import Student  
from .forms import StudentForm  
from django.views.generic.edit import CreateView  
  
class StudentCreate(CreateView):  
    model = Student  
    fields = '__all__'
    success_url = '/n'

  

from django.views.generic.list import ListView

class StudentRetrieve(ListView):
    model = Student


from django.views.generic.detail import DetailView

class StudentDetail(DetailView):
    model = Student


from django.views.generic.edit import UpdateView
class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'
    success_url = '/n'

from django.views.generic.edit import DeleteView

class StudentDelete(DeleteView):
    model = Student
    success_url = '/'
