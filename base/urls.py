from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # path("room",views.room, name="room"),
    path("room/<int:pk>", views.room_number, name="room_number"),
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<str:pk>/", views.updateRoom, name="update-room"),
    path("delete-room/<str:pk>/", views.deleteRoom, name="delete-room"),
    path("login", views.loginPage, name="login"),
]
