from django.urls import path
from .views import profile, signup,login,search,logout,result


urlpatterns = [
    path('signup', signup, name='signup'),
    path('login',login, name='login'),
    path('search', search, name="search"),
    path('logout',logout, name='logout'),
    path('profile/',profile),
    path('result/',result),
    
    
]