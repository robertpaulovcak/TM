from django.contrib import admin

# Register your models here.
from tm_app.models import Person, Task


class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'id'
    ]

class TaskAdmin(admin.ModelAdmin):
    list_display = [
        'task_name',
        'person',
        'status',

    ]

admin.site.register(Person, PersonAdmin)
admin.site.register(Task, TaskAdmin)