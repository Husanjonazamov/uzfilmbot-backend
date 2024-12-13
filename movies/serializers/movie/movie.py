# movies/serializers.py

from rest_framework import serializers
from movies.models.movie import Movie, Episode


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class EpisodeSerializers(serializers.ModelSerializer):
    class Meta:
      model = Episode
      fields = '__all__'

        

