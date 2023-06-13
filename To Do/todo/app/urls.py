from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='homepage'),
    path('login/',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('signup/',Signup),
    path('add-todo/',add_todo)
]
