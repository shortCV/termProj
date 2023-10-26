# Create your views here.
from django.shortcuts import render
from .models import Task, Songs, Artists, Albums


def search(request):
    searched = request.POST['search']  # get inputted search text (i.e. what you're searching for)
    songs = Songs.objects.filter(title__icontains=searched)
    artists = Artists.objects.filter(name__icontains=searched)
    albums = Albums.objects.filter(title__icontains=searched)

    if request.method == 'POST':
        return render(request, 'search_direct.html', {'searched': searched, 'songs': songs, 'artists': artists, 'albums': albums}) # pass the search results through dict.
    else:
        return render(request, 'search_direct.html', {})


def index(request):
    songs = Songs.objects.all()
    artists = Artists.objects.all()
    albums = Albums.objects.all()
    return render(request, 'index.html', {'songs': songs, 'artists': artists, 'albums': albums})
