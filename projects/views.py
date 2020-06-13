from django.shortcuts import render
from projects.models import Project, Project_post

# Create your views here.\

def projects(request):
    post = Project.objects.all()
    context = {
        "posts": post

    }
    return render(request, 'projects.html', context)



def project_posts(request, uuid):
    post = Project_post.objects.filter(project = uuid)
    context = {
        "posts": post

    }
    return render(request, 'project_posts.html', context)

def projects_index(request, uuid, index):
    project = Project_post.objects.all().filter(project = uuid)
    post = project.get(post_number = index)
    context = {
        "posts": post

    }
    return render(request, 'projects_index.html', context)

