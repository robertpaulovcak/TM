# Create your views here.

from django.shortcuts import render, redirect, resolve_url
from django.views import View
from django.views.generic import CreateView

from tm_app.forms import TaskForm, PersonForm
from tm_app.models import Person, Task

#Createyourviewshere.

from django.template.response import TemplateResponse



# def PersonList(request):
#     person = Person.objects.all()
#     context = {
#         'person': person,
#     }
#     return TemplateResponse(request, 'personlist.html', context=context)

class PersonListView(View):

    def get(self, request, *args, **kwargs):
        person = Person.objects.all()
        context = {
            'person': person,
        }
        return TemplateResponse(request, 'personlist.html', context=context)


def TaskListOrd(request):
    task_ord = Task.objects.order_by('status')
    #name = Person.objects.filter(name=)
    context = {
        'task_ord': task_ord,
        #'name': name
    }
    return TemplateResponse(request, 'tasklist.html', context=context)

# def TaskListPer(request, pk):
#     list_per = Person.objects.get(id=pk)
#     list_ord = Task.objects.order_by('-status')
#     context = {
#         'list_per': list_per,
#         'list_ord': list_ord,
#     }
#     return TemplateResponse(request, 'persontasklist.html', context=context)

class TaskListPerView(View):

    def get(self, request, pk, *args, **kwargs):
        list_per = Person.objects.get(id=pk)
        list_ord = Task.objects.order_by('-status')
        context = {
            'list_per': list_per,
            'list_ord': list_ord,
        }
        return TemplateResponse(request, 'persontasklist.html', context=context)

def homepage(request):
    tasklist = Task.objects.order_by('-status')
    #person_name = Task.person()
    context = {
        'tasklist': tasklist,
        #'pername': person_name,
    }

    return TemplateResponse(request, 'homepage.html', context=context)

class CreateTaskView(CreateView):
    template_name = 'create_task.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return resolve_url('itemlist', pk=self.object.id)


class CreatePersonView(CreateView):
    template_name = 'create_person.html'
    form_class = PersonForm
    model = Person

    def get_success_url(self):
        return resolve_url('tasklist', pk=self.object.id)





