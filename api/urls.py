from django.urls import path
from api.views.api import (
                    MoviesList,
                    CategoryList,
                    TreylerList,
                    EpisodeList,
                    UsersList
                    )

from treyler.views.treyler import TreylerDetail
from season.views.season import SeasonDetailView, SeasonListByMovieCode
from movies.views import MovieDetail, EpisodesBySeriesCodeView, DownloadCount, CategoryGetMovie



urlpatterns = [
    # users views
    path('users/', UsersList.as_view(), name='users'),

    # movie views
    path('movies_list/', MoviesList.as_view(), name='movies_list'),
    path('movies_category/<str:title>', CategoryGetMovie.as_view(), name='category_movie'),
    path('movies/<str:code>/', MovieDetail.as_view(), name='movie-detail'),
    path('download_count/<int:code>/', DownloadCount.as_view(), name='download_count'),
    path('series/<str:code>/episodes/', EpisodesBySeriesCodeView.as_view(), name='episode'),

    # api views 
    path('category_list/', CategoryList.as_view(), name='category_list'),
    path('episode/', EpisodeList.as_view(), name='episode_list'),
    path('season/', EpisodeList.as_view(), name='episode_list'),
    path('treyler/', TreylerList.as_view(), name='treyler_list'),

    # treyler views
    path('treyler/<str:title>/', TreylerDetail.as_view(), name='treyler_detail'),
   
    # season views
    path('movies/<str:code>/seasons/', SeasonListByMovieCode.as_view(), name='season_list_by_movie_code'),
    path('seasons/<int:season_id>/', SeasonDetailView.as_view(), name='season-detail'),
    
]
