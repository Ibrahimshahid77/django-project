import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()
User = get_user_model()
user = User.objects.get(username='retro')
user.is_superuser = True
user.save()
print(f"{user.username} is now a superuser.")
user = User.objects.get(username='ibrahim777')
user.is_superuser = False
user.save()                                 
print(f"{user.username} is no longer a superuser.")
#for user in User.objects.values():
   # print(user)
total_users = User.objects.count()
print("Total users:", total_users)
latest_users = User.objects.order_by('date_joined')
for user in latest_users:
    print(user.username, user.date_joined)

user_id = "4"
try:
    user = User.objects.get(id=int(user_id)) 
    print(user.username)
except User.DoesNotExist:
    print("User not found.")

is_active = str(User.objects.get(username="ibrahim").is_active)
print("USER ACTIVE:", user.is_active, )



