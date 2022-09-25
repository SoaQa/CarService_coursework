from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('admin/', views.admin),

]
