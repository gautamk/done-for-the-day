from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models


class GoogleUser(AbstractUser, models.Model):
    profile_picture = models.URLField(blank=True)
