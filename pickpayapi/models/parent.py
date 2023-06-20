from django.db import models
from django.contrib.auth.models import User


class Parent(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name= models.CharField(max_length=25)
    last_name= models.CharField(max_length=25)
    email= models.CharField(max_length=50)
    password= models.CharField(max_length=25)
    monthly_budget= models.IntegerField(default= 0)
