# django and restframework import
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# model import
from movies.models.movie import Movie, Category

# serializers import
from movies.serializers.movie.movie import MovieSerializer, EpisodeSerializers



# kinoni code bo'yicha olish
class MovieDetail(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'code'

    def get(self, request, *args, **kwargs):
        code = kwargs.get('code')
        movie = get_object_or_404(Movie, code=code)
        data = {
            "title": movie.title,
            "genre": movie.genre,
            "year": movie.year,
            "quality": movie.quality,
            "language": movie.language,
            "country": movie.country,
        }
        if movie.file_id:
            data["file_id"] = movie.file_id
        else:
            data["movie_file"] = request.build_absolute_uri(movie.movie_file.url)
        return Response(data)



def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movies_detail.html', {'movie': movie})



# qismlarni olish code bo'yicha
class EpisodesBySeriesCodeView(APIView):
    def get(self, request, code):
        try:
            series = Movie.objects.get(code=code)
            episodes = series.episodes.all()
            serializer = EpisodeSerializers(episodes, many=True)
            return Response({'episodes': serializer.data})
        except Movie.DoesNotExist:
            return Response({'error': 'Series not found'}, status=status.HTTP_404_NOT_FOUND)




class DownloadCount(APIView):
    def get(self, request, code):
        try:
            movie = Movie.objects.get(code=code)
            movie.download_count += 1
            movie.save()
            
            return Response(movie.download_count)
        
        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
class CategoryGetMovie(APIView):
    def get(self, request, title):  
        try:
            category = Category.objects.get(title=title)
            movies = Movie.objects.filter(category=category).values()
            return Response(movies, status=200)  
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=404)



