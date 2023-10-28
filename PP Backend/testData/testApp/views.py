# Create your views here.
from django.shortcuts import render, redirect
from .models import Task, Songs, Artists, Albums
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


def search(request):
    searched = request.POST['search']  # get inputted search text (i.e. what you're searching for)
    songs = Songs.objects.filter(title__icontains=searched)
    artists = Artists.objects.filter(name__icontains=searched)
    albums = Albums.objects.filter(title__icontains=searched)

    if request.method == 'POST':
        return render(request, 'search_direct.html', {'searched': searched, 'songs': songs, 'artists': artists,
                                                      'albums': albums})  # pass the search results through dict.
    else:
        return render(request, 'search_direct.html', {})


def index(request):
    songs = Songs.objects.all()
    artists = Artists.objects.all()
    albums = Albums.objects.all()
    return render(request, 'index.html', {'songs': songs, 'artists': artists, 'albums': albums})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, 'register.html', context={"register_form": form})
