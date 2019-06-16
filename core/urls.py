from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', views.dashboard),
]
