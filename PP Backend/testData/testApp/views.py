# Create your views here.
from django.shortcuts import render
from .models import Task, Songs, Artists, Albums


def index(request):
    songs = Songs.objects.all()
    artists = Artists.objects.all()
    albums = Albums.objects.all()
    return render(request, 'index.html', {'songs': songs, 'artists': artists, 'albums': albums})
