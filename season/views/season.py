from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from season.models.season import Season
from movies.models.movie import Movie, Episode
from api.serializers.serializers.serializers import SeasonSerializer, EpisodeSerializers, MovieSerializer 



class SeasonListByMovieCode(APIView):

    def get(self, request, code):
        try:
            movie = Movie.objects.get(code=code)
        except Movie.DoesNotExist:
            return Response({"detail": "Movie not found."}, status=status.HTTP_404_NOT_FOUND)

        episodes = Episode.objects.filter(series=movie)
        season_ids = episodes.values_list('season', flat=True).distinct()

        seasons = Season.objects.filter(id__in=season_ids)

        serializer = SeasonSerializer(seasons, many=True)

        # Javob qaytarish
        return Response({"seasons": serializer.data})




class SeasonDetailView(APIView):
    def get(self, request, season_id):
        try:
            code = request.GET.get('code')
            if not code:
                return Response({'error': 'Code parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

            season = Season.objects.get(id=season_id)

            movies = Movie.objects.filter(season=season, code=code)
            movie_serializer = MovieSerializer(movies, many=True)

            episodes = Episode.objects.filter(season=season, series__code=code)
            episode_serializer = EpisodeSerializers(episodes, many=True)

            return Response({
                'movies': movie_serializer.data,
                'episodes': episode_serializer.data
            })
        except Season.DoesNotExist:
            return Response({'error': 'Season not found'}, status=status.HTTP_404_NOT_FOUND)
