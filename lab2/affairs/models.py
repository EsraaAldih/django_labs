
from django.db import models

    
class Intake(models.Model):
    id =models.AutoField(primary_key=True)
    fullname =models.CharField(max_length=20,default='intake42')
    sdate =models.DateField()
    edate =models.DateField()


class Track(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default='os')

class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    bdate=models.DateField()
    intake=models.CharField(max_length=20)
    track=models.CharField(max_length=20)
    # intake=models.ForeignKey('Intake',default=1,on_delete=models.CASCADE)
    # track=models.ForeignKey('Track',default=1,on_delete=models.CASCADE)