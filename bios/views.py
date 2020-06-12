from django.shortcuts import render
from bios.models import Bio

# Create your views here.

def bios(request):
    "people = Bio.objects.all()"
    people = ["Jason", "Kyle", "Adriane", "Jill", "Bob"]
    peoplegrp3 = []
    newgrp = []
    for i in range(len(people)):
        newgrp.append(people[i])
        print(i)
        if i % 3 == 2 or i == len(people) - 1:
            peoplegrp3.append(newgrp)
            newgrp = []


  
    context = {
        "group" : peoplegrp3
    }

    return render(request, 'bios.html', context)

