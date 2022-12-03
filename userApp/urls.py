
from django.contrib import admin
from django.urls import path, include
from userApp import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('register',views.reg, name='register'),
    path('reg',views.Register,name='reg'),
    path('login',views.Login,name='login'),
    path('login-view',views.loginView,name='loginView'),
    path('bank-form', views.Bank,name='bank-form'),
    path('logout',views.logout,name='logout')
]