from django.shortcuts import render
from events.models import Event

# Create your views here.


    
def events(request):
    post = Event.objects.all()
    context = {
        "posts": post

    }
    return render(request, 'events.html', context)

def events_index(request, uuid):
    post = Event.objects.get(uuid = uuid)
    context = {
        "posts": post

    }
    return render(request, 'events_index.html', context)

