from django.db import models
from django.contrib.auth.models import User


class Parent(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_budget= models.IntegerField(default= 0)
