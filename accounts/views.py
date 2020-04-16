from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    # pass # nothing will happen/ignore without error
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2: 
            messages.info(request, "password does not match")
            return redirect("accounts:register")
        elif User.objects.filter(username=username).exists():
            messages.info(request, "username already exists")
            return redirect("accounts:register")
        elif User.objects.filter(email=email).exists():
            messages.info(request, "email address already exists")
            return redirect("accounts:register")
        else:
            user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            return redirect("accounts:login")
    
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid username or password")
            return redirect("accounts:login")

def logout(request):
    auth.logout(request)
    return redirect("/")

def loggedinuser(request):
    # method 1 using request.user.is_authenticated
    print(request.user.is_authenticated)
    if request.user.is_authenticated == False:
        return redirect("accounts:login")
    else:
        return render(request, 'only-logged-in-user.html')

# method 2 for access only logged in user
@login_required(login_url='/accounts/login/')
def loggedinuserv2(request):
    return render(request, 'only-logged-in-user.html')