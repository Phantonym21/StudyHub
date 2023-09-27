from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm
from django.contrib.auth.models import User,auth
from django.contrib import messages

rooms = [
    {"id": 1, "name": "CM punk"},
    {"id": 2, "name": "John Cena"},
    {"id": 3, "name": "Daniel Bryan"},
    {"id": 4, "name": "Rey Mysterio"},
]


def home(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q)
    )

    room_count = rooms.count()
    topics = Topic.objects.all()

    context = {"room": rooms, "topics": topics, "room_count": room_count}
    return render(request, "base/home.html", context)


def room(request):
    return render(request, "base/room.html", {"context": "room"})


def room_number(request, pk):
    room = "No such room"

    room = Room.objects.get(id=pk)
    # for i in rooms:
    #     if pk == i['id']:
    #         room = i
    #         break
    context = {"room": room}
    return render(request, "base/room.html", context)


def createRoom(request):
    form = RoomForm
    if request.method == "POST":
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "base/room_form.html", context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "base/delete.html", {"obj": room})
    # pass


def loginPage(request):
    if request.method=='POST':
        username =  request.POST.get('username')
        password =  request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User doesn't exist")
    context = {}
    return render(request, "base/login_register.html", context)
