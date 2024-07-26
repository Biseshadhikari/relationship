from django.urls import path
from .views import *
urlpatterns = [
    path('profile/<int:userid>',profile)
]
