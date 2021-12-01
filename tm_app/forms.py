from django import forms

from tm_app.models import Task, Person


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'status', 'person'] #alebo ['__all__'] pouzi vsetky fields ktore ma model Task

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name']

class Homepage(forms.ModelForm):
    pass



