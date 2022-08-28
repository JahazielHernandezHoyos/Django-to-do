from django.urls import path
from crud import views

urlpatterns = [
    path("task/", views.task, name="task")
]
