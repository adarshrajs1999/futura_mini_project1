from datetime import datetime

from django.db import models

# Create your models here.

class Todo(models.Model):
        name=models.CharField(max_length=250)
        salary=models.IntegerField()
        dob=models.DateField(blank=True,null=True)
        bio=models.TextField()