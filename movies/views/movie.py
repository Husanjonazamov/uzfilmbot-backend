# django and restframework import
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# model import
from movies.models.movie import Movie, Category

# serializers import
from movies.serializers.movie.movie import MovieSerializer, EpisodeSerializers

from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q




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



class SearchMovie(APIView):

    def search_movies_trigram(self, query):
        """
        Qidirishni funksiyasining asosiy servisi
        """
        return Movie.objects.annotate(
            similarity_title=TrigramSimilarity('title', query),
            similarity_genre=TrigramSimilarity('genre', query),
            similarity_language=TrigramSimilarity('language', query),
            similarity_country=TrigramSimilarity('country', query),
            similarity_quality=TrigramSimilarity('quality', query),
            similarity_code=TrigramSimilarity('code', query),
        ).filter(
            Q(similarity_title__gt=0.1) | Q(similarity_genre__gt=0.1) |
            Q(similarity_language__gt=0.1) | Q(similarity_country__gt=0.1) |
            Q(similarity_quality__gt=0.1) | Q(similarity_code__gt=0.1)
        ).order_by(
            '-similarity_title', '-similarity_genre', '-similarity_language',
            '-similarity_country', '-similarity_quality', '-similarity_code'
        )

    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '') 
        if query:
            movies = self.search_movies_trigram(query) 
            if movies:
                movie_list = [
                    {
                        'title': movie.title,
                        'code': movie.code,
                        'genre': movie.genre,
                        'language': movie.language,
                        'country': movie.country,
                        'quality': movie.quality,
                    }
                    for movie in movies
                ]
                return Response(movie_list)
        else:
            return Response({'status': 'error', 'message': 'Query parameter is missing.'}, status=status.HTTP_400_BAD_REQUEST)

