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
        return '%s' % self.name


class Songs(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ManyToManyField(Artists)
    # https://stackoverflow.com/questions/2029295/django-datefield-default-options
    date = models.DateField(default=datetime.now)
    length = models.DurationField(default=timedelta)

    def __str__(self):
        # https://stackoverflow.com/questions/39883950/str-returned-non-string-type-tuple
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
    # https://stackoverflow.com/questions/39527289/associating-users-with-models-django
    # https://stackoverflow.com/questions/44026548/getting-typeerror-init-missing-1-required-positional-argument-on-delete
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    song = models.ManyToManyField(Songs)

    def __str__(self):
        return '%s %s' % (self.title, self.song)


class Reviews(models.Model):
    song = models.ForeignKey(Songs, on_delete=models.CASCADE, default="1")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="1", related_name="user")
    title = models.CharField(max_length=100, default="Name")
    review = models.CharField(max_length=600)
    rating = models.FloatField()
    likes = models.ManyToManyField(User, default=None, blank=True, related_name="likes")

    def __str__(self):
        return '%s' % self.song

    @property
    def amount_likes(self):
        return self.likes.all().count()

# https://www.youtube.com/watch?v=xqFM6ykQEwo
LIKE_UNLIKE = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_UNLIKE, default='Like', max_length=10)

    def __str__(self):
        return str(self.review)