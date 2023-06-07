from django.db import models
from django.contrib.auth.models import User
from user.models import AllUser , Freelancer

import uuid
# Create your models here.

class Room(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    
    first_user =models.ForeignKey(User,related_name='first_user',on_delete=models.CASCADE,null=True)
    
    second_user = models.ForeignKey(Freelancer,related_name='second_user',on_delete=models.CASCADE,null=True)


class Message(models.Model):
    user = models.ForeignKey(User,related_name="messages",verbose_name="Kullanıcı",on_delete=models.CASCADE)
    room = models.ForeignKey(Room,related_name="messages",verbose_name="Oda",on_delete=models.CASCADE)
    content = models.TextField(verbose_name="Mesaj İçeriği")
    created_at = models.DateTimeField(auto_now_add=True)
    