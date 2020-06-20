from django.shortcuts import render
from bios.models import Bio

# Create your views here.\

def bios(request):
    people = Bio.objects.all()
    boardGroups = []
    groups = []
    pastBoardGroups = []
    pastGroups = []
    
    group3 = []
    for i in range(len(people)):
        if people[i].board and not people[i].past:
            group3.append(people[i])
        if len(group3) == 3 or i == len(people)-1 and not len(group3)== 0:
            boardGroups.append(group3)
            group3 = []

    for i in range(len(people)):
        if not people[i].board and not people[i].past:
            group3.append(people[i])
        if len(group3) == 3 or i == len(people)-1 and not len(group3)== 0:
            groups.append(group3)
            group3 = []

    for i in range(len(people)):
        if people[i].board and people[i].past:
            group3.append(people[i])
        if len(group3) == 3 or i == len(people)-1 and not len(group3)== 0:
            pastBoardGroups.append(group3)
            group3 = []

    for i in range(len(people)):
        if not people[i].board and people[i].past:
            group3.append(people[i])
        if len(group3) == 3 or i == len(people)-1 and not len(group3)== 0:
            pastGroups.append(group3)
            group3 = []

    print("groups: {}".format(groups))
    print("pastGroups: {}".format(pastGroups))

    context = { 
        "board": boardGroups,
        "groups": groups,
        "pastBoard": pastBoardGroups,
        "pastGroups": pastGroups
    }

    return render(request, 'bios.html', context)

