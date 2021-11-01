from django.urls import path
from . import views

urlpatterns = [
    # path('',views.placeholder,name='placeholder'),
    path('<str:q_pk>',views.quiz, name='Quiz'),
    path('end/',views.endquiz, name='endquiz'),
]