from django.contrib import admin
from .models import Room,Message



@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['first_user','second_user']

    class Meta:
        model=Room

@admin.register(Message)
class MassageAdmin(admin.ModelAdmin):
    list_display = ['user', 'room','created_at']

    class Meta:
       model = Message
