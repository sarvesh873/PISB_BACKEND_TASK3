from django.shortcuts import render

def timerpage(request):
    return render(request,'Timer/Base.html')
