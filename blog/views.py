from django.shortcuts import render
from .models import *


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/event.html', context)


'''
def Event(request):
    contet = {
        'events': Event.objects.all()
    }
    return render(request, 'blog/event.html', contet)
'''
