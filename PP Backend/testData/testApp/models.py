# Create your models here.
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    out = models.BooleanField(default=False)
    released = models.DateTimeField
