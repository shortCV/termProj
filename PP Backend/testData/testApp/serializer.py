from rest_framework import serializers
from .models import Songs, Artists, Albums, Playlist, User

class ArtSeri(serializers.ModelSerializer):
    name = serializers.CharField(max_length=500)
    class Meta:
        model = Artists
        fields = '__all__'


class SongsSeri(serializers.ModelSerializer):
    cover_url = serializers.SerializerMethodField()

    artist = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Songs
        fields = ('title', 'artist',  'cover_url')

    def get_cover_url(self, song):
        request = self.context.get('request')
        cover_url = song.cover.url
        return request.build_absolute_uri(cover_url)




class UsersSeri(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
