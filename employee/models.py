from distutils.command import upload
from importlib.resources import path
from django.db import models

# Create your models here.

    
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)  
    photo = models.ImageField(upload_to='images/',null= True)
    father_name = models.CharField(max_length=70,null= True) 
    age = models.IntegerField(default=True)
    address= models.CharField(max_length=350,null= True)
    class Meta:  
        db_table = "employee"  
   
