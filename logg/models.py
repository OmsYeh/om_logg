from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Loggs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

