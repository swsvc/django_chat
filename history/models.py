from django.conf import settings
from django.db import models


class Room(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text[:20]