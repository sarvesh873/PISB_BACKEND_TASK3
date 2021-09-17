from os import name
from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    # path('', views.home, name='glad-home'),
    path('', views.about, name='glad-about'),
]
