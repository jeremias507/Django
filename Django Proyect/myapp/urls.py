from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name="index"),
    path('about/',views.about, name="about"),
    path('hello/<int:id>',views.hello, name="hello"),
    path('tasks/',views.tasks, name="tasks"),
    path('create_task/',views.create_task, name="index"),
    path('projects/',views.proyects, name="create_project"),
    path('create_project/',views.create_project, name="create_task"),
    

]