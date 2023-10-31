# Create your views here.
from django.shortcuts import render, redirect
from django import forms
from .models import Task, Songs, Artists, Albums, Playlist, Reviews, Like
from .forms import NewUserForm, ReviewForm, CreatePlayForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__, static_folder='static')


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
    reviews = Reviews.objects.all()
    return render(request, 'index.html',
                  {'songs': songs, 'artists': artists, 'albums': albums, 'playlists': playlists, 'reviews': reviews})


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
    if request.method == "POST":
        form = ReviewForm(request.POST)  # form creates new user
        if form.is_valid():
            form.save()  # <-- saving the form to the database
            return redirect("index")  # go back to index when form goes through
            # if form isn't valid
        messages.error(request, "Unsuccessful . Invalid information.")

    form = ReviewForm()
    return render(request, 'index.html', context={"review_form": form})


@app.route('/create_play', methods=['POST'])
def create_play(request):
    if request.method == "POST":
        form = CreatePlayForm(request.POST)  # form creates new user
        if form.is_valid():
            form.save()  # <-- saving the form to the database
            return redirect("index")  # go back to index when form goes through
            # if form isn't valid
        messages.error(request, "Unsuccessful . Invalid information.")

    form = CreatePlayForm()
    return render(request, 'index.html', context={"create_play_form": form})


@app.route('/like_review', methods=['POST'])
def like_review(request):
    # https://www.youtube.com/watch?v=xqFM6ykQEwo
    user = request.user # get user
    if request.method == "POST":
        review_id = request.POST.get('review_id')  # get hidden input with Reviews id
        review_element = Reviews.objects.get(id=review_id)  # get review model

        if user in review_element.likes.all():  # if user has already liked review
            review_element.likes.remove(user)  # remove as they've pressed unlike
        else:
            review_element.likes.add(user)  # like review as user has not liked it yet

        like, created = Like.objects.get_or_create(user=user, review_id=review_id)  # define Like model

        if not created:
            if like.value == 'Like':  # change like model value
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()  # save like
    return redirect("index")  # direct back to homepage
