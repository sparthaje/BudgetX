from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login

def index(request):
    return HttpResponseRedirect('/signup/')

def signup_handler(request):
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    new_user = User.objects.create_user(username = username, password = password, email = email)
    new_user.save()
    return HttpResponseRedirect('/signup/')

def signup(request):
    return render(request, 'login/signup.html')

def login_handler(request):
    username = request.POST["usr"]
    password = request.POST["pss"]
    user = authenticate(request, username = username, password = password)
    print(user)
    if user is not None:
        dj_login(request, user)
    else:
        return HttpResponseRedirect('/signup/')
    return HttpResponseRedirect('/upload/')
