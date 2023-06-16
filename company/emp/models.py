from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Employee(models.Model):
    employee_regno = models.IntegerField(unique=True)
    employee_name = models.CharField(max_length=20)
    employee_email = models.EmailField(unique=True)
    employee_mobile = models.BigIntegerField(unique=True, validators=[RegexValidator("^[0-9]{10}$")])
    created_at = models.DateTimeField(auto_now=True)