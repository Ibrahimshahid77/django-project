from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('signup/', views.signup, name='signup_post'),  
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name ='home-page'),
    path('logout/', views.logout_view, name = 'logout'),
    path('contact/', views.contact, name = 'contact'), 
    path('addprof/', views.add_profile, name='add_profile'),
    path('addproj/', views.add_project, name='add_project' ),
    path('viewprof/', views.view_profile, name='view_profile')
]