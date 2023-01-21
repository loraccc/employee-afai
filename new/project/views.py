from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from project.models import Employee
# Create your views here .

def login_user(request):
    return render(request,'login.html')

def INDEX(request):
    emp=Employee.objects.all()
    context={'emp':emp,}

    return render(request,'index.html',context)