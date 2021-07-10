from django.urls import path
from . import views

urlpatterns = [
    path('event/', views.home, name='event'),
    path('', views.home, name='blog-home')
    #path('event/', views.Event, name='event'),
]
