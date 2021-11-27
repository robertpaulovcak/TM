

# Create your models here.
from django.db import models

#Createyourmodelshere.

class Person(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name} : {self.id}'


class Task(models.Model):
    ACTIVE = 'AC'
    CLOSED = 'CL'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (CLOSED, 'Closed'),
    ]
    task_name = models.CharField(max_length=256)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(to='Person', on_delete=models.CASCADE, related_name='task')


    def __str__(self):
        return f'{self.task_name} : {self.person} : {self.status} '
