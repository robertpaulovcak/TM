# Create your views here.

from django.shortcuts import render
from tm_app.models import Person, Task

#Createyourviewshere.

from django.template.response import TemplateResponse

def PersonList(request):
    person = Person.objects.all()
    context = {
        'person': person,
    }
    return TemplateResponse(request, 'personlist.html', context=context)

def TaskListOrd(request):
    task_ord = Task.objects.order_by('-status')
    context = {
        'task_ord': task_ord,
    }
    return TemplateResponse(request, 'tasklist.html', context=context)

def TaskListPer(request, pk):
    list_per = Person.objects.get(id=pk)
    list_ord = Task.objects.order_by('-status')
    context = {
        'list_per': list_per,
        'list_ord': list_ord,
    }
    return TemplateResponse(request, 'persontasklist.html', context=context)