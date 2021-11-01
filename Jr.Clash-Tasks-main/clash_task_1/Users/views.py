from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import extendeduser
import re
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['uname'], password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return redirect('profile')
        else:
            return render(request, 'Users/login.html', {'error': "Invaild Crededntials"})
    else:
        return render(request, 'Users/login.html')


def register(request):
        if request.method == "POST":

            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request, 'Users/register.html', {'error': "username already exist"})

                except User.DoesNotExist:
                    # user = User.objects.create_user(username=request.POST['username'],password= request.POST['password1'],email= request.POST['email'])
                    # user = User.objects.create_user(username=request.POST['username'],password= request.POST['password1'])
                    number = request.POST['number']
                    year = request.POST['year']


                if (len(request.POST['password1']) < 10):
                    return render(request, 'Users/register.html', {'error': "Password too Short, Should Contain ATLEAST 1 Uppercase,1 lowercase,1 special Character and 1 Numeric Value"})

                elif not re.search(r"[\d]+", request.POST['password1']):
                    return render(request, 'Users/register.html', {'error': "Your Password must contain Atleast 1 Numeric value "})
                elif not re.findall('[A-Z]', request.POST['password1']):
                    return render(request, 'Users/register.html', {'error': "Your Password must contain Atleast 1 UpperCase Letter "})

                elif not re.findall('[a-z]', request.POST['password1']):
                    return render(request, 'Users/register.html', {'error': "Your Password must contain Atleast 1 lowercase Letter "})
                elif not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', request.POST['password1']):
                    return render(request, 'Users/register.html', {'error': "Your Password must contain Atleast 1 Specail character "})
                elif not re.findall('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', request.POST['email']):
                       return render(request, 'Users/register.html', {'error': "Email ID is not Valid"})

                else:
                    
                    if extendeduser.objects.filter(number=number):
                        return render(request, 'Users/register.html', {'error': "phonenumber already exist try using another one"})
                    else:
                        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'],email=request.POST['email'],first_name=request.POST['firstname'],last_name=request.POST['lstname'])
                        newextendeduser = extendeduser( number=number, year=year, user=user)
                        newextendeduser.save()
                        auth.login(request, user)
                        messages.success(
                            request, f'Your account has been Create!! Login Now')

                        return redirect(login)
            else:
                return render(request, 'Users/register.html', {'msg': ["Passwords Don't match"]})
        else:
            return render(request, "Users/register.html")


def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    datas = extendeduser.objects.filter(user = request.user)
    return render(request,'Users/profile.html',{'data':datas})

def Qpage(request):
    return render(request,'Users/login.html')