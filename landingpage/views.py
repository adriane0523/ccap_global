from django.shortcuts import render
from landingpage.models import Video
from events.models import Event
from projects.models import Project




def landingpage(request):
    post = Video.objects.all()
    projects = Project.objects.all().filter(front_page = True)
    events = Event.objects.all().filter(front_page = True)
    context = {
        "posts": post,
        "projects": projects,
        "events": events,

    }
    return render(request, 'landing_page.html', context)



