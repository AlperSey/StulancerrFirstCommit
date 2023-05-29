from django.shortcuts import render

# Create your views here.


def chat_view(request):
    return render(request, "chat/index.html")

def user_room_view(request, room_name):
    context = dict(
        room_name = room_name
    )
    return render(request, "chat/new_mesaj.html", context)




# def user_chat_view(request):
#     return render(request, "chat/index.html")

# def freelancer_chat_view(request):
#     return render(request, "chat/index.html")