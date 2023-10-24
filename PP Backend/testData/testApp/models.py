# Create your models here.
from django.db import models
from datetime import datetime
import django.utils.timezone
from datetime import timedelta, datetime


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)


class Artists(models.Model):
    name = models.CharField(max_length=100)


class Songs(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artists)
    date = models.DateField(default=datetime.now)
    length = models.DurationField(default=timedelta)


class Albums(models.Model):
    title = models.CharField(max_length=200)
    song = models.ManyToManyField(Songs)
    artist = models.ManyToManyField(Artists)
    date = models.DateField(default=datetime.now)
    length = models.DurationField(default=timedelta)
