from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

