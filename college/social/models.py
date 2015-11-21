from django.db import models

# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    usertype=models.CharField(max_length=10)
    year=models.IntegerField(null=True)
    branch=models.CharField(max_length=300,blank=True)
                        
class announcements(models.Model):
     name=models.CharField(max_length=20)
     text=models.CharField(max_length=10000)
     time=models.TimeField()

class complaints(models.Model):
     name=models.CharField(max_length=20)
     text=models.CharField(max_length=10000)
     time=models.TimeField()
    
class assignments(models.Model):
     name=models.CharField(max_length=20)
     text=models.FileField()
     time=models.TimeField()

class curriculum(models.Model):
     name=models.CharField(max_length=20)
     text=models.CharField(max_length=10000)
     time=models.TimeField()
     
    

