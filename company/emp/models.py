from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_regno = models.TextField(unique=True)
    employee_name = models.TextField()
    employee_email = models.TextField()
    employee_mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

class Staff(models.Model):
    sjoin = models.DateField()
    sname = models.CharField(max_length=20)
    semail = models.EmailField(max_length=30)
    smobile = models.IntegerField(max_length=10)
    creat_at = models.DateTimeField(auto_now=True)
