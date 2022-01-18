from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm
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

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'base/delete.html', {'obj': room})