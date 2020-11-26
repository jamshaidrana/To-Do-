from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path(r'add_todo/',views.add_todo, name='addToDo'),
    path(r'delete_todo/<int:todo_id>/',views.delete_todo, name='deleteToDo'),


]
