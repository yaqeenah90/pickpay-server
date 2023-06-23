from django.db import models
from django.contrib.auth.models import User


class Child(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    financial_goal = models.IntegerField(default =3)
