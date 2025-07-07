from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
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
        
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'index.html', {'error': 'Email invalid'})   
        if User.objects.filter(username=username).exists():
            return render(request, 'index.html', {'error': 'Username used'})
        if User.objects.filter(email=email).exists():
            return render(request, 'index.html', {'error': 'Email used'})   
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
            return render(request, 'login.html',{'error': 'Wrong username or password'})
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('/login/')
@login_required
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')
def button(request):
    return render(request, 'button.html')

@login_required
def add_profile(request):
    if request.method == 'POST':
        if Profile.objects.filter(user=request.user).exists():
            return redirect('view_profile')
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.skills = request.POST.get('skills')
        profile.about = request.POST.get('about')
        profile.save()
        return redirect('view_profile')
    return render(request, 'profile.html')

def add_project(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
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
       
        return redirect('view_profile')
    return render(request, 'profile.html') 

@login_required
def view_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        projects = Project.objects.filter(profile=profile)
    except Profile.DoesNotExist:
        return redirect('add_profile')
    return render(request, 'view_profile.html', {
        'profile': profile,
        'projects': projects}) 
def guest(request):
    users_with_profiles = User.objects.filter(profile__isnull=False)
    users_without_profiles = User.objects.filter(profile__isnull=True)
    users = list(users_with_profiles) + list(users_without_profiles)
    return render(request, 'guest.html', {'users': users})

def manager_view(request):
    if not request.user.is_superuser:
        return HttpResponse("You are not the manager")
    users_with_profiles = User.objects.filter(profile__isnull=False)
    users_without_profiles = User.objects.filter(profile__isnull=True)
    users = list(users_with_profiles) + list(users_without_profiles)
    return render(request, 'manager.html', {'users': users})

def delete_user(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('manager_view')



         
 





        









    
