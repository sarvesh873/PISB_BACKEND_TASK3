from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=500)
    option_1 = models.CharField(max_length=500)
    option_2 = models.CharField(max_length=500)
    option_3 = models.CharField(max_length=500)
    option_4 = models.CharField(max_length=500)
    
    class Answer(models.IntegerChoices):
        option_1 = 1
        option_2 = 2
        option_3 = 3
        option_4 = 4

    correct_ans = models.IntegerField(choices=Answer.choices)
    def __str__(self):
        return self.question

class UserResponse(models.Model):
    user      = models.ForeignKey(User, on_delete=CASCADE)
    question  = models.ForeignKey(Question, on_delete=CASCADE, null=True)
    class Answer(models.IntegerChoices):
        option_1 = 1
        option_2 = 2
        option_3 = 3
        option_4 = 4

    selected_option = models.IntegerField(choices=Answer.choices, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}: {self.question} - {self.selected_option}"

