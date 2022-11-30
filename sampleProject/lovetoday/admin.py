from django.contrib import admin
# from lovetoday.models import Employee
from lovetoday.models import Student
# Register your models here.
# class EmployeeAdmin(admin.ModelAdmin):
#     emp_details = ['empNo','empName','empSalary','empAddress']


class StudentAdmin(admin.ModelAdmin):
    student_details = ['student_No','student_Name','student_Class','student_Address']

    
    
admin.site.register(Student,StudentAdmin) 
