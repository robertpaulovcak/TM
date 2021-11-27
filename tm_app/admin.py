from django.contrib import admin

# Register your models here.
from tm_app.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]

admin.site.register(Person, PersonAdmin)