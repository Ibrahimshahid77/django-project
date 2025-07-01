from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'index.html', {'error': 'Invalid email'})
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('/login/') 
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            print("Loggin")
            return redirect('/home/')
        else:
            print("dafa ho")
            return render(request, 'login.html', {'error': 'Wrong Password'})
    
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')






    
