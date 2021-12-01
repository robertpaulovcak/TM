# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import BaseDeleteView

from tm_app.forms import TaskForm, PersonForm
from tm_app.models import Person, Task


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

# def TaskListOrd(request):
#     task_ord = Task.objects.order_by('status')
#     #name = Person.objects.filter(name=)
#     context = {
#         'task_ord': task_ord,
#         #'name': name
#     }
#     return TemplateResponse(request, 'tasklist.html', context=context)

class TaskListOrdView(View):

    def get(self, request, *args, ** kwargs):
        task_ord = Task.objects.order_by('status')
        person = Person.objects.all()
        context = {
            'task_ord': task_ord,
            'person': person,
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
def Homepage(request):
    context = {
        'homepage': 'This is out Task Manger homepage'
    }
    return TemplateResponse(request, 'homepage.html', context=context)


class TaskListPerView(View):

    def get(self, request, pk, *args, **kwargs):
        list_per = Person.objects.get(id=pk)
        list_ord = Task.objects.order_by('-status')
        context = {
            'list_per': list_per,
            'list_ord': list_ord,
        }
        return TemplateResponse(request, 'persontasklist.html', context=context)


class CreateTaskView(CreateView):
    template_name = 'create_task.html'
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy('tasklist')
    #
    # def get_success_url(self):
    #     return resolve_url('itemlist', pk=self.object.id)


class CreatePersonView(CreateView):
    template_name = 'create_person.html'
    form_class = PersonForm
    model = Person
    success_url = reverse_lazy('tasklist')

class TaskUpdateView(UpdateView):
    template_name = 'create_task.html'
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy('tasklist')

class DeleteTaskView(DeleteView):
    template_name = 'create_task.html'
    model = Task
    success_url = reverse_lazy('tasklist')


class LogInView(LoginView):
    form_class = AuthenticationForm
    authentication_form = None
    redirect_field_name = 'tasklist'
    template_name = 'registrations/login.html'
    redirect_authenticated_user = False
    extra_context = None









