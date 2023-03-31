from django.db import models

from profiles.models import User


class Room(models.Model):
    """
    Room represents a chat room.
    It contains an online field for tracking when users
    connect and disconnect from the chat room.
    """

    name = models.CharField(max_length=128)
    signed_up_users = models.ManyToManyField(to=User, blank=True, related_name="signed_up_user")
    online = models.ManyToManyField(to=User, blank=True, related_name="online_user")
    # If it's private, then it's a two people/organization chat.
    # Else, it's a group chat.
    private = models.BooleanField(default=True)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f"{self.name} ({self.get_online_count()})"


class Message(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}: {self.content} [{self.timestamp}]"
