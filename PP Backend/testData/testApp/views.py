# Create your views here.
from django.shortcuts import render
from .models import Task, Songs, Artists, Albums

def search (request):
    if request.method == 'post':
        return render(request, 'search_direct.html', {})
    else:
        return render(request, 'search_direct.html', {})
def index(request):
    songs = Songs.objects.all()
    artists = Artists.objects.all()
    albums = Albums.objects.all()
    return render(request, 'index.html', {'songs': songs, 'artists': artists, 'albums': albums})
