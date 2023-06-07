from django.contrib import admin
from django.urls import path
from . import views

app_name = "chat"


urlpatterns = [ 
    
    path('messages/',views.chat_view,name='chat_view'),
    path("<str:room_name>/", views.user_room_view, name='user_room_view'),
    path('startChat/<str:all_user>/',views.startChat,name='startChat')
    


]