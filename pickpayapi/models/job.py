from django.db import models


class Job(models.Model):

    title= models.CharField(max_length=30)
    description= models.CharField(max_length=350)
    rate= models.IntegerField()
    assigned_to= models.ManyToManyField("Child", related_name="assigning")
    parent= models.ForeignKey("Parent", on_delete=models.CASCADE)
