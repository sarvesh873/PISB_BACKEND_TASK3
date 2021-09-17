"""task34 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from task3 import views as task3_views
from django.conf.urls import url
from task3.views import login
# from task3 import url 
from task3.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
   
    # path('task3/', task3_views.register, name="register"),
    # # path('profile/', task3_views.profile, name='profile'),
    # path('login/', auth_views.LoginView.as_view(template_name='task3/login.html'), name="login"),
    # path('home/', auth_views.LogoutView.as_view(template_name='task3/home.html'), name="home"),
    # path('search', task3_views.search, name="search"),
    # path('task3/', login),
    path('task3/', include('task3.urls')),
    # path('login/', auth_views.LoginView.as_view(template_name='api/login.html'), name="login"),
    url(r'^search/$', search),
    path('search/', task3_views.search, name='search'),
    
    

    
    
    
]