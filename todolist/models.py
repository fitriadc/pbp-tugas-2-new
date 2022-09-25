from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Todolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(datetime.now())
    title = models.CharField(max_length=280)
    description = models.TextField()
