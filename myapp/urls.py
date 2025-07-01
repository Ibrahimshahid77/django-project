from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),    
    path('signup/', views.signup, name='signup_post'),  
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name ='home-page')
]
