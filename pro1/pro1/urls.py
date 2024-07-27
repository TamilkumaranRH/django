"""
URL configuration for pro1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app2.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',details_form,name='DetailsForm'),
    path('n',details_list,name='DetailsList'),
    path("n1/<int:pk>",details_update,name='DetailsUpdate'),
    path('ss/', set_session, name='set_session'),
    path('gs/', get_session, name='get_session'),
    path('sc/', set_cookie, name='set_cookie'),
    path('gc/', get_cookie, name='get_cookie'),
    path("login",login,name="alogin"),
    path("logout",logout,name="logout"),
    path("dashboard",dashboard,name="dashboard")
]
