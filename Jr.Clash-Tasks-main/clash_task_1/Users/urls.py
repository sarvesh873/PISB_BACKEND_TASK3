from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('Qpage/',views.Qpage, name='Qpage'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
]
