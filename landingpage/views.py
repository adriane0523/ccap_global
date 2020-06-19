from django.shortcuts import render
from landingpage.models import Video
from events.models import Event
from projects.models import Project




def landingpage(request):
    post = Video.objects.all()

    context = {
        "posts": post,
   

    }
    return render(request, 'landing_page.html', context)



