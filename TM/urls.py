"""TM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from tm_app.views import TaskListPerView, PersonListView, CreateTaskView, CreatePersonView, TaskListOrdView, \
    TaskUpdateView, LogInView, Homepage, DeleteTaskView

urlpatterns = [
    path('registrations/login', LogInView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('personlist/', PersonListView.as_view(), name='personlist'),
    path('tasklist/', TaskListOrdView.as_view(), name='tasklist'),
    path('persontasklist/<int:pk>/', TaskListPerView.as_view(), name='persontasklist'),
    path('create_task/', CreateTaskView.as_view(), name='create_task'),
    path('create_person/', CreatePersonView.as_view(), name='create_person'),
    path('update_task/<int:pk>/', TaskUpdateView.as_view(), name='update_task'),
    path('homepage/', Homepage, name='homepage'),
    path('delete_task/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),
]

