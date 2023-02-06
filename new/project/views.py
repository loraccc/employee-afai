from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from project.models import Employee

from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from .serializers import EmployeeSerializer

# API VIEWS 
# API VIA CLASS 
class EmployeeApiview(APIView):   # postman ma + headers ma gayera Content-Type ani vlaue=App/json hanesi dekhauxa

    def get(self,request):
        emp=Employee.objects.all()
        serializer=EmployeeSerializer(emp,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):            # browser bata data lina leko post method le 
        data={
            "Name":request.POST.get("Name"),
            "Email":request.POST.get("Email"),
            "Address":request.POST.get("Address"),   #postman bata form bata garda sajilo
            "Phone":request.POST.get("Phone"),
        }   

        serializer=EmployeeSerializer(data=data)       #employeeserializer lai serialize gareko 
        if serializer.is_valid():       
            serializer.save()       
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class EmpIDApiview(APIView):
    def get_emp(self,id):
        try:
            data=Employee.objects.get(id=id)
            return data
        except Employee.DoesNotExist:
            return None
        
    def get(self,request,id):
        Emp_instance=self.get_emp(id)    # def ma vako name le get garniii

        if not Emp_instance:
            return Response({"error":"data not found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=EmployeeSerializer(Emp_instance)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,id):
        emp_instance=self.get_emp(id=id)
        if not emp_instance:
            return Response(EmployeeSerializer.errors,status=status.HTTP_404_NOT_FOUND)
        data={
            "Name":request.POST.get("Name"),
            "Email":request.POST.get("Email"),
            "Address":request.POST.get("Address"),   #postman bata form bata garda sajilo
            "Phone":request.POST.get("Phone"),
        }
        serializer=EmployeeSerializer(instance=emp_instance,data=data,partial=True)
        if serializer.is_valid():
            return Response(EmployeeSerializer.data,status=status.HTTP_200_OK)
    
    def delete(self, request, id):
        emp_instance = self.get_object(id)

        if not emp_instance:
            return Response({"error": "Data not found"}, status=status.HTTP_404_NOT_FOUND)

        emp_instance.delete()
        return Response({"msg": "Data deleted"}, status=status.HTTP_200_OK)


def login_user(request):
    if request.method=="post":
        name=request.POST.get('name')
        password=request.POST.get('password')
        emp=Employee(
            Name=name,
            password=password,
        )
        emp.save()
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
    emp=Employee.objects.all()  #{{forloop.counter}} chai div id ma rakhni so that tya click garda value awos
    context={
        'emp':emp
    }
    return render(request,'index.html',context)

def UPDATE(request,id):
    if request.method=="POST":
        emp=Employee.objects.get(id=id)
        emp.Name=request.POST.get('name')
        emp.Email=request.POST.get('email')
        emp.Address=request.POST.get('address')
        emp.Phone=request.POST.get('phone')
        emp.save()
        return redirect('index')
    
    return redirect(request,'index.html')

def DELETE(request,id):
    emp=Employee.objects.filter(id=id)
    emp.delete()
    context={
        'emp':emp,
    }
    return redirect('index')
    return render(request,'index.html')

def Base(request):
    return render(request,'base.html')