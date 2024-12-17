# django and restframeword import
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

# modeli import
from movies.models.movie import Movie, Category, Episode
from season.models.season import Season
from treyler.models.treyler import Treyler
from users.models.users import User

from api.serializers.serializers.serializers import (
    MovieSerializer,
    TreylerSerializers,
    EpisodeSerializers,
    UsersSerializer,
    Category_Serializer,
    SeasonSerializer
)




# movies list class
class MoviesList(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# treyler list class
class TreylerList(generics.ListCreateAPIView):
  queryset = Treyler.objects.all()
  serializer_class = TreylerSerializers


# category list class
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer


# episode list class
class EpisodeList(generics.ListAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializers


# users list class
class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    
    
# season list class   
class SeasonList(generics.ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    
    
