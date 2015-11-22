from django.db import models

# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    usertype=models.CharField(max_length=10)
#year=models.IntegerField()
    branch=models.CharField(max_length=10)
                            