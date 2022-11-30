from django.shortcuts import render
from lovetoday.models import Student
from . import forms

# Create your views here.

def display(request):
    return render(request,'lovetoday/index.html')

# def dbdemo(request):
#     data = Employee.objects.all()
#     emp_dict = {'emp_detail':data}
#     return render(request,'lovetoday/dbdemo.html',context=data)

def empform(request):
    form= forms.FormInfo()
    formDict = {'form':form}
    return render(request,'lovetoday/form.html',context=formDict)


def cookiesCount(request):
    count = request.COOKIES.get('count',0)
    totalcount = int(count)+1
    response = render(request,'lovetoday/cookie.html',{'count':totalcount})
    response.set_cookie('count',totalcount)
    return response


def sessioncount(request):
    count = request.session.get('count',0)
    totalcount = int(count)+1  
    request.session['count'] = totalcount
    print(request.session.get_expiry_date())
    return render(request,'lovetoday/session.html',{'count':totalcount})

def studentDetails(request):
    student = Student.objects.all()
    return render(request,'lovetoday/studentdetails.html',{'student':student})  