from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class BigintField(models.Field):
    def db_type(self):
        return 'BIGINT(20)'

class Staff(models.Model):
    sjoin = models.DateField()
    sname = models.CharField(max_length=20)
    semail = models.EmailField(max_length=30)
    smobile = models.BigIntegerField(unique=True, validators=[RegexValidator("^[0-9]{10}$")])
    creat_at = models.DateTimeField(auto_now=True)