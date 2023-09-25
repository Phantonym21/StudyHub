from django.shortcuts import render
from django.http import HttpResponse
from . models import Room

rooms= [
    {'id':1,'name':"CM punk"},
    {'id':2,'name':"John Cena"},
    {'id':3,'name':"Daniel Bryan"},
    {'id':4,'name':"Rey Mysterio"}
]

def home(request):
    rooms = Room.objects.all()
    context = {'room':rooms}
    return render(request,"base/home.html",context)

def room(request):
    
    return render(request,"base/room.html",{"context":"room"})

def room_number(request,pk):
    room = "No such room"

    room = Room.objects.get(id = pk)
    # for i in rooms:
    #     if pk == i['id']:
    #         room = i
    #         break
    context ={"room":room}
    return render(request,"base/room.html",context)



