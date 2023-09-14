from django.urls import path
from .views import *

urlpatterns = [
    path('', userpage, name='userpage'),
    path('userpage', userpage, name='userpage'),
    path('login', loginPage, name='login'),
    path('register', registerPage, name='register'),
    path('me', me, name='me'),
    path('main', main, name='main'),
    path('logout', doLogout, name='logout'),
    path('update_mission/<mission_id>', update_mission, name='update-mission'),
    path('delete_mission/<mission_id>', delete_mission, name='delete-mission'),
    ]
