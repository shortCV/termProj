# Create your views here.
from django.shortcuts import render, redirect
from django import forms
from .models import Task, Songs, Artists, Albums, Playlist, Reviews
from .forms import NewUserForm, ReviewForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__, static_folder='static')
from django.http import HttpResponse


def search(request):
    # https://www.youtube.com/watch?v=AGtae4L5BbI
    searched = request.POST['search']  # get inputted search text (i.e. what you're searching for)
    songs = Songs.objects.filter(title__icontains=searched)  # any songs that contain the inputted search
    artists = Artists.objects.filter(name__icontains=searched)  # any artists that contain the inputted search
    albums = Albums.objects.filter(title__icontains=searched)  # any albums that contain the inputted search

    if request.method == 'POST':  # when user submits search
        return render(request, 'search_direct.html', {'searched': searched, 'songs': songs, 'artists': artists,
                                                      'albums': albums})  # pass the search results through dict.
    else:
        return render(request, 'search_direct.html', {})


def play(request):
    results = request.GET['filter']  # get selected playlist from dropdown
    songs = Songs.objects.all()
    artists = Artists.objects.all()
    albums = Albums.objects.all()
    playlists = Playlist.objects.all()
    return render(request, 'playlist_display.html',
                  {'songs': songs, 'artists': artists, 'albums': albums, 'playlists': playlists, 'filter': results})


def index(request):
    songs = Songs.objects.all()
    artists = Artists.objects.all()
    albums = Albums.objects.all()
    playlists = Playlist.objects.all()
    return render(request, 'index.html', {'songs': songs, 'artists': artists, 'albums': albums, 'playlists': playlists})


# https://ordinarycoders.com/blog/article/django-user-register-login-logout
def register_request(request):
    if request.method == "POST":  # when user is directed to register page
        form = NewUserForm(request.POST)  # form creates new user

        if form.is_valid():
            user = form.save()  # user input is saved
            login(request, user)  # login user
            messages.success(request, "Registration successful.")  # user feedback
            return redirect("index")  # go back to index when form goes through

        # if form isn't valid
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm()
    return render(request, 'register.html', context={"register_form": form})


def login_request(request):
    if request.method == "POST":  # when user is directed to login page
        form = AuthenticationForm(request, data=request.POST)  # pre-built django authentication form

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)  # validates users input of credentials

            if user is not None:
                login(request, user)  # login user
                messages.info(request, f"You are now logged in as {username}.")  # user feedback
                return redirect("index")  # direct back to homepage
            else:
                messages.error(request, "Invalid username or password.")  # if user gets login wrong
        else:
            messages.error(request, "Invalid username or password.")  # if form isn't valid

    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)  # logs out user
    messages.info(request, "You have successfully logged out.")  # user feedback
    return redirect("index")  # direct user back to homepage


@app.route('/publish_review', methods=['POST'])
def publish_review(request):
    if request.method == "POST":  # when user is directed to register page
        form = ReviewForm(request.POST)  # form creates new user
        if form.is_valid():
            form.save() #<-- saving the form to the database
            return redirect("index")  # go back to index when form goes through
            # if form isn't valid
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = ReviewForm()
    return render(request, 'index.html', context={"review_form": form})
