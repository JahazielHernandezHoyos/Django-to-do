import imp
from pydoc import describe
from django.db import models
from django.contrib import admin
from crud.views import task

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=108)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.name
        
admin.site.register(Task)
