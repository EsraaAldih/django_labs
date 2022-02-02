"""lab2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Register.views import login
from Register.views import logout
from Register.views import registeruser
from affairs.views import create,retrieve, edit,update,delete
from affairs.views import search_trainee
from affairs.views import create_Form ,insertStudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login),
    path('logout/',logout,name="logout"),
    path('register', registeruser),
    path('create',create),
    path('home',retrieve),
    path('edit/<int:id>', edit ,name="edit"),
    path('update/<int:id>',update,name="update"),
    path('delete/<int:id>',delete,name="delete"),
    path('search',search_trainee,name="search"),
    path('Form',create_Form,name="Form"),
    path('insertStudent',insertStudent,name="insertStudent"),
    
]
