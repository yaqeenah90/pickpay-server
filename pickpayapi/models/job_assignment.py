from django.db import models

class JobAssignment(models.Model):
    job= models.ForeignKey("Job", on_delete=models.CASCADE)
    child= models.ForeignKey("Child", on_delete=models.CASCADE)
    completed= models.BooleanField(default=False)
