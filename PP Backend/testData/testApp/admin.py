from django.contrib import admin
from .models import Task, Songs, Artists, Albums, Playlist

admin.site.register(Task)
admin.site.register(Songs)
admin.site.register(Artists)
admin.site.register(Albums)
admin.site.register(Playlist)

