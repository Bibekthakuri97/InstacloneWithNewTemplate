from django.contrib import admin
from django.urls import path,include
from user_app.views import display,loginauth,logout,register

app_name = 'user'

urlpatterns = [
    path('login',loginauth,name='login'),
    path('logout',logout,name='logout'),
    path('register',register,name='register'),
]
