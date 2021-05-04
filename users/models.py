from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class Book(models.Model):
    title = models.TextField(max_length=32, blank=False, null=False)


class User(AbstractUser):

    nickname = models.CharField(max_length=10, default="lim")
    supervisor = models.BooleanField(default=False)
    birth = models.DateField(default=date.today)
    student_number = models.CharField(max_length=7, default="C000000")
