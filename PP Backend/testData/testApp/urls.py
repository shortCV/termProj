"""
URL configuration for testData project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search_direct', views.search, name='search-direct'),
    path("playlist_display", views.play, name="playlist_display"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path('publish_review', views.publish_review, name='publish_review'),
    path('create_play', views.create_play, name='create_play'),
    path('like_review', views.like_review, name='like_review'),
    path('api/get_songs/', views.get_songs, name='get_songs'),
    path('api/get_artist/', views.get_artist, name='get_artist'),
    path('api/get_albums/', views.get_albums, name='get_albums'),
    path('api/get_reviews/', views.get_reviews, name='get_reviews'),


]
