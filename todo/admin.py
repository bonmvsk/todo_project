from django.contrib import admin

from .models.todo import ToDo

# Register your models here.
admin.site.register(ToDo)