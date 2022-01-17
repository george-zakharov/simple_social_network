from django.shortcuts import render
from .models import Room
# TODO: FOR TEST
# from django.http import HttpResponse

# TODO: TEST
# rooms = [
#     {'id': 1, 'name':'Lets learn python'},
#     {'id': 2, 'name':'Lets learn design'},
#     {'id': 3, 'name':'Lets learn devops'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)
    # TODO: FOR TEST
    # return HttpResponse('Home page')

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
    # TODO: FOR TEST
    # return HttpResponse('ROOM')