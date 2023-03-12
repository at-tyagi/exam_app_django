from django.shortcuts import render
from django.http import HttpResponse
from test_app.models import Employee


def greeting(request):
    s="<h1>Hello World !!<h1>"
    return HttpResponse(s)


def about(request):
    msg='this is about page'
    return render(request,'test_app/about.html',{'msg':msg})

def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    return render(request,'test_app/employees.html',context=data)

def showContact(request):
    s="<h1>This is conatct !!<h1>"
    return HttpResponse(s)
