from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    date_event = models.DateTimeField(default=timezone.now)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


'''
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_event = models.DateTimeField(default=timezone.now)
   # location=models.
    co_ordinator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
'''
