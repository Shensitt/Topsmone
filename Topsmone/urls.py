"""
Topsmone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from os import name
from re import T
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import login
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from App import forms, views
from datetime import datetime


from App.views import anketa, contacts_page, index_page,  about_page, phones_page, registration

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('',index_page),
    path('admin/', admin.site.urls),
    path('about',views.about_page, name="about_page"),
    path('phones',phones_page),
    path('contacts', anketa),
    path('registration', registration, name='registration'),
    #path("accounts/", include("django.contrib.auth.urls")), 
    path('blog', views.blog, name='blog')
]
