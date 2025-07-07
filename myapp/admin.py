from django.contrib import admin
from .models import User
from .models import Profile,Project

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Project)

