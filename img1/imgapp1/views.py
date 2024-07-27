from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import requests
from.forms import StudentsForm
# Create your views here.
def t6(y):
    
    """ 
     base_url="https://api.artic.edu/api/v1/artworks"
     response = requests.get(base_url)
     artworks= response.json()
     for artwork in artworks['data']:
          pass
     
     return render(y,"date1.html",{'artworks':artworks,'data':artwork}) """
    
    base_url="https://http.dog/423.json"
    response=requests.get(base_url)
    dog=response.json()
    return render(y,"date1.html",{'dog':dog})

def student_form(request):
    if request.method=='POST':
        form=StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('StudentsList')
    else:
              form = StudentsForm()
              return render(request, 'save.html', {'form': form})
        
from.models import students
def student_list(request):
     student= students.objects.all()
     return render(request,"list.html",{'students':student})

def student_update(request, pk):
    student = get_object_or_404(students, pk=pk)

    if request.method == "POST":
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list.html')
    else:
        form = StudentsForm(instance=student)

    return render(request, 'update.html', {'form': form})