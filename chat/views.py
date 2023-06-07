from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from user.models import AllUser , Freelancer
from .models import Room
# Create your views here.


def chat_view(request):
    users = AllUser.objects.all().exclude(all_user_user_name=request.user)
    context = dict(
        users=users
    )
    return render(request, "chat/index.html",context)

def user_room_view(request, room_name):
    context = dict(
        room_name = room_name
    )
    return render(request, "chat/new_mesaj.html", context)

def startChat(request,username):
    second_user = AllUser.objects.get(username=username)
    try:
        room = Room.objects.get(first_user=request.user,second_user=second_user)
    except Room.DoesNotExist:
        room = Room.objects.create(first_user = request.user,second_user=second_user)
    return redirect('index',room.id)




# def user_chat_view(request):
#     return render(request, "chat/index.html")

# def freelancer_chat_view(request):
#     return render(request, "chat/index.html")