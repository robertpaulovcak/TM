# Create your views here.

from django.shortcuts import render
from tm_app.models import Person, Task

#Createyourviewshere.

from django.template.response import TemplateResponse

def PersonList(request):
    person=Person.objects.all()
    context={
        'person': person,
    }
    return  TemplateResponse(request, 'personlist', context=context)
