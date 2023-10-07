from django.db import models
class Details(models.Model):
    uname=models.CharField(max_length=20)
    passw=models.EmailField()
    # def __str__(self):
    #     return self.name
class A_Details(models.Model):
    uname1=models.CharField(max_length=20)
    passw1=models.EmailField()