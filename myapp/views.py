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
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

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
        if len(username) < 5:
            messages.error(request, "Username must be at least 5 characters long.")
            return redirect('signup')
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
            return redirect('/home/')
        else:
            return render(request, 'login.html',{'error': 'Wrong username or password'})
    return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('/login/')
@login_required
def home(request):
    profiles = Profile.objects.all()
    return render(request, 'home.html',{'profiles': profiles})

def contact(request):
    return render(request, 'contact.html')
def button(request):
    return render(request, 'button.html')

@login_required
def add_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)


    if request.method == 'POST':
        if request.POST.get('skills'):
         profile.skills = request.POST.get('skills')
        if request.POST.get('about'):
         profile.about = request.POST.get('about')
        if request.FILES.get('profile_picture'):
            profile.profile_picture = request.FILES.get('profile_picture')
        profile.save()
        return redirect('view_profile')
    return render(request, 'profile.html', {'profile': profile})

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
       
        return HttpResponse("Project saved")
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
        return HttpResponse("You are not manager")
    users_with_profiles = User.objects.filter(profile__isnull=False)
    users_without_profiles = User.objects.filter(profile__isnull=True)
    users = list(users_with_profiles) + list(users_without_profiles)
    return render(request, 'manager.html', {'users': users})

def delete_user(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('manager_view')
def profile_detail(request, user_id):
    profile = Profile.objects.get(user__id=user_id)
    projects = profile.project_set.all()
    return render(request, 'profile_detail.html', {'profile': profile, 'projects': projects})
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not request.user.check_password(current_password):
            messages.error(request, 'Wrong password.')
        elif new_password == current_password:
            messages.error(request, 'Password can not be the same as old')
        elif new_password != confirm_password:
            messages.error(request, 'New passwords are not same.')
       
        elif len(new_password) < 6:
            messages.error(request, 'Password should be atleast 6 numbers long')
        elif len(new_password) > 12:
             messages.error(request, 'Password should not be longer than 12 characters')
        elif not any(char.isdigit() for char in new_password):
              messages.error(request, 'Password must have at least one number')
        else:
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Password changed successfully.') 
            return redirect('home-page')
           
            
    return render(request, 'new_password.html')








         
 





        









    
