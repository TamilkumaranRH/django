from django.shortcuts import render,redirect,get_object_or_404
from .forms import DetailsForm

def details_form(request):
    if request.method == 'POST':
        form = DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DetailsForm()
    return render(request, 't.html', {'form': form})

#list
from.models import details
def details_list(request):
    detail = details.objects.all()
    return render(request, 'listDetails.html', {'details': detail})
# Create your views here.

#update
def details_update(request, pk):
    detail = get_object_or_404(details, pk=pk)

    if request.method == "POST":
        form = DetailsForm(request.POST, instance=detail)
        if form.is_valid():
            form.save()
            return redirect('listDetails.html')
    else:
        form = DetailsForm(instance=detail)

    return render(request, 'update.html', {'form': form})


""" def t6(r):
    return render(r,"t.html") """
from django.shortcuts import render, redirect
from django.http import HttpResponse

def set_session(request):
    request.session['name'] = 'John Doe'
    return HttpResponse('Session data set')

def get_session(request):
    name = request.session.get('name', 'Session data not set')
    return HttpResponse(f'Session data: {name}')

def set_cookie(request):
    response = HttpResponse('Cookie data set')
    response.set_cookie('name', 'Jane Doe', max_age=3600)  # Cookie expires in 1 hour
    return response

def get_cookie(request):
    name = request.COOKIES.get('name', 'Cookie data not set')
    return HttpResponse(f'Cookie data: {name}')



#Login and dashboard


def login(r):
    if 'un' in r.session:
        return redirect("dashboard")
    else:
        if r.method=="POST":
            username=r.POST.get("username")
            password=r.POST.get("password")
            if( password=="admin"):
                r.session['un'] = username
                return redirect("dashboard")
        else:
            return render(r,"login.html")
            

def dashboard(r):
    if 'un' in r.session:
        name=r.session["un"]
        return render(r,"dashboard.html",{"name":name})
    else:
        return redirect('alogin')

def logout(request):
    if 'un' in request.session:
        del request.session['un']  # Clear department ID from session
    return redirect('alogin')