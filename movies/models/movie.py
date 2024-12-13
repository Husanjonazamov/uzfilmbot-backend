# models.py
from django.db import models
from django.contrib.postgres.indexes import GinIndex
from season.models.season import Season



class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, blank=True, null=True)
    year = models.IntegerField()
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    quality = models.CharField(max_length=25)
    file_id = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=50, unique=True)
    download_count = models.IntegerField(default=0)


    class Meta:
        indexes = [
            GinIndex(fields=['title'], name='title_gin_trgm_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['genre'], name='genre_gin_trgm_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['language'], name='language_gin_trgm_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['country'], name='country_gin_trgm_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['quality'], name='quality_gin_trgm_idx', opclasses=['gin_trgm_ops']),
            GinIndex(fields=['code'], name='code_gin_trgm_idx', opclasses=['gin_trgm_ops']),
        ]

    def __str__(self):
        return self.title

    @staticmethod
    def search(query):
        from django.contrib.postgres.search import TrigramSimilarity
        from django.db.models import Q
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


class Episode(models.Model):
    series = models.ForeignKey(Movie, related_name='episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, blank=True, null=True)
    year = models.IntegerField()
    language = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    quality = models.CharField(max_length=25)
    file_id = models.CharField(max_length=255, blank=True, null=True)
    episode_number = models.IntegerField()
    download_count = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.series.title} - Episode {self.episode_number}"



 
