# Create your models here.
from django.db import models
from datetime import datetime
import django.utils.timezone
from datetime import timedelta, datetime
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)


class Artists(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.name)


class Songs(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artists)
    date = models.DateField(default=datetime.now)
    length = models.DurationField(default=timedelta)

    def __str__(self):
        return '%s %s %s' % (self.title, self.date, self.artist)


class Albums(models.Model):
    cover = models.ImageField(upload_to='cover_pic', default='default.jpg')
    title = models.CharField(max_length=200)
    song = models.ManyToManyField(Songs)
    artist = models.ManyToManyField(Artists)
    date = models.DateField(default=datetime.now)
    length = models.DurationField(default=timedelta)

    def __str__(self):
        return '%s %s %s' % (self.title, self.date, self.artist)


class Playlist(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    song = models.ManyToManyField(Songs)

    def __str__(self):
        return '%s %s' % (self.title, self.song)
