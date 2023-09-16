from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    # path("room",views.room, name="room"),
    path("room/<int:pk>",views.room_number, name="room_number")
]