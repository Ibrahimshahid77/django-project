from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import User, Profile, Project
from django.contrib.auth import authenticate, login as auth_login,logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        context = {}
        try:
            validate_email(email)
        except ValidationError:
            context['error'] = 'Invalid email'
            return render(request, 'index.html', context)
    
        
        if User.objects.filter(username=username).exists():
            context['error'] = 'Username used'
            return render(request, 'index.html', context)
        if User.objects.filter(email=email).exists():
            context['error'] = 'Email used'
            return render(request, 'index.html', context)   
        
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('/login/') 
    return render(request, 'index.html')

def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            print("Loggin")
            return redirect('/home/')
        else:
            context['error']= 'Wrong username or password'
            return render(request, 'login.html',context)
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('/login/')
@login_required
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')


@login_required
def add_profile(request):
    if request.method == 'POST':
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.skills = request.POST.get('skills')
        profile.about = request.POST.get('about')
        profile.save()

        names = request.POST.getlist('project_name')
        urls = request.POST.getlist('project_url')
        des = request.POST.getlist('project_des')
        stacks = request.POST.getlist('project_stack')
        photos = request.FILES.getlist('project_photo')

        for i in range(len(names)):
            Project.objects.create(
            profile=profile,
            name=names[i],
            url=urls[i],
            description=des[i],
            stack=stacks[i],
            photo=photos[i])

        return redirect('/home/')

    return render(request, 'profile.html')






        









    
