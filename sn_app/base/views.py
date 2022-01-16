from django.shortcuts import render
# TODO: FOR TEST
# from django.http import HttpResponse

rooms = [
    {'id': 1, 'name':'Lets learn python'},
    {'id': 2, 'name':'Lets learn design'},
    {'id': 3, 'name':'Lets learn devops'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)
    # TODO: FOR TEST
    # return HttpResponse('Home page')

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
    # TODO: FOR TEST
    # return HttpResponse('ROOM')