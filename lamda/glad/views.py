from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
    if request.method == "POST" :
      number = int(request.POST["number"])
      if (number>0):
             result = [n for n in range(1, number+1)]
             return render(request, 'glad/about.html' , { "solnum": result })

      else:
           return render(request, 'glad/positive.html'  )
             
    else:
        return render(request, 'glad/home.html'  )
        