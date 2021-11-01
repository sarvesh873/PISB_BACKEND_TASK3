from django.urls import path
from . import views

urlpatterns = [
    path('timer/',views.timerpage, name='timer'),
]