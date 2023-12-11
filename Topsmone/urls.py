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
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from App import forms, views
from datetime import datetime
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from App.views import anketa, contacts_page, index_page,  about_page, phones_page, registration

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('',index_page),
    path('admin/', admin.site.urls),
    path('about',views.about_page, name="about_page"),
    path('phones',views.phones, name='phones'),
    path('phonesCam',views.phonesCam, name='phonesCam'),
    path('phonesCPU',views.phonesCPU, name='phonesCPU'),
    path('phonesTop',views.phonesTop, name='phonesTop'),
    path('contacts', anketa),
    path('registration', registration, name='registration'),
    path('blog', views.blog, name='blog'),
    path('orders', views.orders, name='orders'),
    path('ordersmanager', views.ordersmanager, name='ordersmanager'),
    path('shoppingcart', views.shoppingcart, name='shoppingcart'),
    path('add_to_shoppingcart', views.add_to_shoppingcart, name='add_to_shoppingcart'),
    path('newpost', views.newpost, name='newpost'),
    path('newproduct', views.newproduct, name='newproduct'),
    path('videopost', views.videopost, name='videopost'),
    path('blogpost/<int:parametr>',views.blogpost, name='blogpost'),
    path('phone/<int:parametr>',views.phone, name='phone'),
    path('login/',
         LoginView.as_view
         (
             template_name='login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Вход',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout')
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()