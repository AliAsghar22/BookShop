from django.contrib.auth.models import User
from django.db import models


class User(models.Model, User):
    token = models.CharField(max_length=48)