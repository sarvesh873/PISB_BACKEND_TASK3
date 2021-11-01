from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from .models import *

def quiz(request, q_pk):
    if request.method == 'POST':
        if request.POST['save_n_next'] == 'save_n_next':
            que = Question.objects.get(pk = int(q_pk)-1)
            selected_option = int(request.POST.get('user_response', 0))
            try:
                user_res = UserResponse.objects.get(question = que, user = request.user)
                user_res.selected_option = selected_option
                user_res.save()
            except UserResponse.DoesNotExist:
                inst = UserResponse(user = request.user, question = que, selected_option = selected_option)
                inst.save()
                print("saved yayy!!!!!!!")
    if int(q_pk) > 10:
        return redirect('/quiz/10')

    question = Question.objects.get(pk = q_pk)
    try:
        user_res = UserResponse.objects.get(question = question, user = request.user) 
        print(user_res.selected_option)
    except UserResponse.DoesNotExist:
        user_res = None
    next = question.pk +1
    prev = question.pk -1
    context = {'question':question, 'next':next, 'prev':prev, 'user_res':user_res}
    return render(request,'Quiz/Qpage.html', context)

def placeholder(request):
    return HttpResponse('<h1>Placeholder</h1>')

def endquiz(request):
    if request.method == 'POST':
        if request.POST['end'] == "timeUp":
            messages.info(request, "Oops!! Time's Up. Quiz submitted automatically.")
        elif request.POST['end'] == "submitted":
            messages.success(request, "Quiz Submitted Succesfully.")
        # return render(request, 'Quiz/endQuiz.html')
        return redirect('login')