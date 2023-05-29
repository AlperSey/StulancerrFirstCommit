# from django.db import models
# from django.contrib.auth.models import User
# from user.models import AllUser

# import uuid
# # Create your models here.

# class Room(models.Model):
#     id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    
#     all_user =models.ForeignKey(User,related_name='all_user_room',on_delete=models.CASCADE,null=True)
    
#     freelancer = models.ForeignKey(AllUser,related_name='freelance_room',on_delete=models.CASCADE,null=True)


# class Message(models.Model):

    