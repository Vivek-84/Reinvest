from django.db import models

# Create your models here.
from django.db import models
import time

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()     
    def __str__(self):
        return self.name
       

class Service(models.Model):
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    address=models.CharField(max_length=200)
    streetaddress=models.CharField(max_length=122)
    city=models.CharField(max_length=250)
    state=models.CharField(max_length=100)
    abc=models.CharField(max_length=100)
    status=models.CharField(max_length=100,default="")
    residential=models.CharField(max_length=100, default='')
    ybd=models.DateField(time.timezone , default=None)
    dop=models.DateField(time.timezone , default=None)
    famt=models.TextField(default='')
    asf=models.TextField( default='')
    loan=models.TextField(default='')
    desc=models.TextField(default='')
    

    def __str__(self):
        return self.name

    

