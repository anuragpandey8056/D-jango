from django.db import models
from datetime import datetime

# Create your models here.

class Adhar(models.Model):
    aadharNo= models.IntegerField(unique=True)
    CreatedDate=models.DateTimeField( auto_now=False, auto_now_add=False)
    createdBY= models.CharField( max_length=50)
    def __str__(self):
        return str(self.aadharNo)

class Student(models.Model):
    Name= models.CharField(max_length=150)
    Email=models.EmailField()
    contact= models.IntegerField()
    address= models.CharField(max_length=254)
    dob= models.DateTimeField( auto_now=False, auto_now_add=False)
    adharno= models.OneToOneField(Adhar,on_delete=models.PROTECT,to_field='aadharNo')
    def __str__(self):
        return str(self.adharno)



