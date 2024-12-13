from django.urls import path
from season.views.season import SeasonListByMovieCode, SeasonDetailView

urlpatterns = [
    path('movies/<str:code>/seasons/', SeasonListByMovieCode.as_view(), name='season_list_by_movie_code'),
    path('seasons/<int:season_id>/', SeasonDetailView.as_view(), name='season-detail'),
]


