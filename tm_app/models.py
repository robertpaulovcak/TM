

# Create your models here.
from django.db import models

#Createyourmodelshere.

class Person(models.Model):
    name=models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}:{self.id}'


class Task(models.Model):
    task_name=models.CharField(max_length=256)
    status=models.CharField(max_length=256)
    created_at=models.DateTimeField(auto_now_add=True)
