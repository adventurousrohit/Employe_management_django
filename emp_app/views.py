import json
from django import http
from django.shortcuts import render
from datetime import datetime

from emp_app.models import Employee


def index(request):
    return render(request,'index.html')


def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method =='POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        salary= int(request.POST['salary'])
        bonous= int(request.POST['bonous'])
        phone= int(request.POST['phone'])
        role= int(request.POST['role'])
        dept= int(request.POST['dept'])
        # hire_date=datetime.now()
        # hire_date= request.POST['hire_date']
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonous=bonous,phone=phone,role_id=role,dept_id=dept,hire_date=datetime.now())
        new_emp.save()
        return http.HttpResponse('Add employee succeful')
    elif request.method == 'GET':
        print('get')
        return render(request,'add_emp.html')
    else:
        return http.HttpResponse('An Excepction occured:Employee')

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            print(emp_id)
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return http.HttpResponse('Employee remove succesfully')
        except:
            return http.HttpResponse('please enter a valid EMP id')
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    return render(request,'filter_emp.html')
