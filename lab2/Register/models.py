from django.db import models

class myuser(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    repeatPassword=models.CharField(max_length=20)
    email= models.EmailField(max_length=70,blank=True,unique=True)