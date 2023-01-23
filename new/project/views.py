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


def ADD(request):
    if request.method=="POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        address= request.POST.get('address')
        phone= request.POST.get('phone')

        emp=Employee(
            Name=name,     # first ko Name models wala and 2nd ma vako name html ko form vitra ko name= ""
            Email=email,
            Address=address,
            Phone=phone,
        )
        emp.save()
        
    return redirect('index') # from views.py name ma vako chiz rakhni 

def EDIT(request):
    emp=Employee.objects.all()
    context={
        'emp':emp
    }
    return render(request,'index.html',context)

def UPDATE(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phone=request.POST.get('phone')

        
        emp=Employee(
            id=id,
            Name=name,
            Email=email,
            Phone=phone,
            Address=address,
        )
        return redirect('index')
    
    return redirect(request,'index.html')

