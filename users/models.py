from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    supervisor = models.BooleanField(default=False)
    cellphoneNum = models.CharField(max_length=13, default="010-0000-0000")
