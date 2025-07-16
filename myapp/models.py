from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(default='')
    skills = models.CharField(max_length=500, default='')
    profile_picture = models.ImageField(upload_to='profile_pics/')
    followers = models.ManyToManyField(User, related_name='following', blank=True) 

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.URLField(blank=True, null = True)
    photo = models.ImageField(upload_to='', blank=True, null = True)
    description = models.TextField(default='')
    stack = models. CharField(max_length=25,default='')
class Comment(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()














































     
