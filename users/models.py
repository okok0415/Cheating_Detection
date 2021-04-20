from django.contrib.auth.models import AbstractUser
from django.db import models


class Book(models.Model):
    title = models.TextField(max_length=32, blank=False, null=False)


class User(AbstractUser):

    nickname = models.CharField(max_length=10, default="lim")
    supervisor = models.BooleanField(default=False)
    cellphoneNum = models.CharField(max_length=13, default="010-0000-0000")
