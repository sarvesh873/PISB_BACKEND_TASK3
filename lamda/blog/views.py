import contextlib
from typing import ContextManager
from django.shortcuts import render

posts = [
    {   
        'author':'surface',
        'title' : 'blog post 2',
        'content': 'first post content',
        'date_passed': 'august30,2022'
        
    },
    {
        'author':'surface',
        'title': 'blog post 2',
        'content': 'first post content',
        'date_passed': 'august30,2022'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html')
    
def num(request):
    return render(request, 'blog/num.html')