from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse  
from django.views import View  

from .models import Student  
from .forms import StudentForm  
def details_form(request):
    print("sdfj")
    if request.method == 'POST':
        print("asjdlkf")
        form = StudentForm(request.POST)
        if form.is_valid():
            print("213")
            form.save()
            return redirect('DetailsForm')
    else:
        print("baslf")
        form = StudentForm()
    return render(request, 'styleapp/index.html', {'form': form})

#list
from.models import Student
def details_list(request):
    detail = Student.objects.all()
    return render(request, 'styleapp/listDetails.html', {'details': detail})

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
