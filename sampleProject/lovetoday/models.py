from django.db import models

# Create your models here.
# class Employee(models.Model):
#     empNo = models.IntegerField()
#     empName = models.CharField(max_length=40)
#     empSalary = models.IntegerField()
#     empAddress = models.CharField(max_length=50)

class Student(models.Model):
    student_No = models.IntegerField()
    student_Name = models.CharField(max_length=50)
    student_Class = models. IntegerField()
    student_Address = models.CharField(max_length=100)
