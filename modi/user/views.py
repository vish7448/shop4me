from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render
from django.http import HttpResponse
from .models import deteail
# Create your views here.
def login_user(request):
    if request.method=="POST":
        login_name=request.POST['name']
        login_password = request.POST['password']
        user_try = authenticate(username=login_name, password=login_password)
        if user_try is not None:
            login(request, user_try)
            print("login succeful")

    return render(request, 'user/login.html')

def signup(request):
    if request.method=='POST':
        name = request.POST['username1']
        user_email = request.POST['email']
        user_password = request.POST['password']
        sign=User.objects.create_user(username=name, email=user_email, password=user_password)
        sign.save()

        det = deteail(user_name=name, user_email=user_email, password=user_password)
        det.save()


    else:
        return render(request, 'user/signup_usr.html')
    return render(request, 'user/signup_usr.html')