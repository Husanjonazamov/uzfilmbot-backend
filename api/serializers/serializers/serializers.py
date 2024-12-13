from rest_framework import serializers
from movies.models.movie import Movie, Category, Episode
from season.models.season import Season
from treyler.models.treyler import Treyler
from users.models.users import User


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TreylerSerializers(serializers.ModelSerializer):
    class Meta:
      model = Treyler
      fields = '__all__'


class EpisodeSerializers(serializers.ModelSerializer):
    class Meta:
      model = Episode
      fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ['id', 'title']
        
        
        

