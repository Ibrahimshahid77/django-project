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
    path('viewprof/', views.view_profile, name='view_profile'),
    path('button/', views.button, name='button'),
    path('guest/', views.guest, name ='guestpage'),
    path('manager/', views.manager_view, name='manager_view'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('profile/<int:user_id>/', views.profile_detail, name='profile_detail'),
    path('password/', views.change_password, name = 'change_pass'),
    path('follow/<int:user_id>/', views.follow_user, name='follow'),
    path('profile/<int:user_id>/', views.comment, name='comment')

]
