from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


YEAR_CHOICE=[
    ("FE","FE"),
    ("SE","SE"),
    ("TE","TE"),
    ("BE","BE"),
    ("Others","Others")

]

class extendeduser(models.Model):


    number = models.CharField(max_length=20,null=True,default="")
    year = models.CharField(max_length=20, choices=YEAR_CHOICE,null=True,default="")
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)

    
    def __str__(self):
        return f'{self.user.username}'