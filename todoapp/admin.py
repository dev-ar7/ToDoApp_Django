from django.contrib import admin
from . import models
from .models import Username, Task

# Register your models here.


class UsernameAdmin(admin.ModelAdmin):
    class Meta:
        model = Username


class TaskAdmin(admin.ModelAdmin):
    class Meta:
        model = Task


admin.site.register(Username, UsernameAdmin)
admin.site.register(Task, TaskAdmin)
