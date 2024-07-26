from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from .models import *


def profile(request,userid): 
    user = User.objects.get(id = userid)
    photos = Photos.objects.filter(user = user)
    context = { 
               'photos':photos
               }
    return render(request,'profile.html',context)
