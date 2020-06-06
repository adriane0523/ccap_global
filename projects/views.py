from django.shortcuts import render
from projects.models import Project

# Create your views here.\

def projects(request):
    post = Project.objects.all()
    context = {
        "posts": post

    }
    return render(request, 'projects.html', context)



def projects_index(request, uuid):
    post = Project.objects.get(uuid = uuid)
    context = {
        "posts": post

    }
    return render(request, 'projects_index.html', context)
