from django.shortcuts import render
from bios.models import Bio
# Create your views here.\

def bios(request):
    people = Bio.objects.all()
    groups = []
    group3 = []
    for i in range(len(people)):
        group3.append(people[i])
        if i % 3 == 2 or i == len(people)-1:
            groups.append(group3)
            group3 = []

    context = {
        "groups": groups

    }
    return render(request, 'bios.html', context)

