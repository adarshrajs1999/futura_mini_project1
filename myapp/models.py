from django.db import models

# Create your models here.

class Todo(models.Model):
        subject=models.CharField(max_length=50)
        data=models.CharField(max_length=100)
        date=models.DateField()