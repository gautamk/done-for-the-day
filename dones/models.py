from django.conf import settings
from django.db import models

__author__ = 'gautam'

User = settings.AUTH_USER_MODEL


class Done(models.Model):
    is_done = models.BooleanField(default=True)
    message = models.CharField(max_length=255, blank=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)