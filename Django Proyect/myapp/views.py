from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import CreateNewTask, CreateNewProject


# Create your views here.
def index(request):
    title = "Django Course!!"
    return render(request, "index.html", {"title": title})


def about(request):
    username = "Ameth"
    return render(request, "about.html", {"username": username})


def hello(request, id):
    print(id)
    return HttpResponse(f"<h1>Hello {id}</h1>")


def proyects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "Projects.html", {"projects": projects})


def tasks(request):
    try:
        tasks = Task.objects.all()
        return render(request, "tasks.html", {"tasks": tasks})
    except ObjectDoesNotExist:
        return HttpResponse("<h1>Task not foud</h1>", status=404)


def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html", {"form": CreateNewTask})
    else:
        Task.objects.create(
            title=request.POST["title"],
            desc1ription=request.POST["description"],
            project_id=1,
        )
        return redirect("tasks")


def create_project(request):
    if request.method == "GET":
        return render(request, "create_project.html", {"form": CreateNewProject})
    else:
        Project.objects.create(name=request.POST["name"])
        redirect('projects')
       