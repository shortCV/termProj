from django.contrib import admin
from .models import Task, Songs, Artists, Albums, Playlist, Reviews, Like

admin.site.register(Task)
admin.site.register(Songs)
admin.site.register(Artists)
admin.site.register(Albums)
admin.site.register(Playlist)
admin.site.register(Reviews)
admin.site.register(Like)

