from django.contrib import admin
from movies.models.movie import Episode, Movie, Category

# Episode modelini Movie admin interfeysida inlayn tarzda ko'rsatish uchun ishlatiladi
class EpisodeInline(admin.TabularInline):
    model = Episode  
    extra = 1 


# Movie modelini admin panelda sozlash uchun ishlatiladi
class MovieAdmin(admin.ModelAdmin):
    inlines = [EpisodeInline]  
    list_display = ('title', 'genre', 'category', 'year', 'quality', 'language', 'country', 'code', 'file_id')
    

# Category modelini admin panelda sozlash uchun ishlatiladi
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',) 


# Episode modelini admin panelda sozlash uchun ishlatiladi
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('series', 'title', 'file_id', 'episode_number', 'download_count',)
    


# Modelni admin panelda ro'yxatdan o'tkazish (faqat bir marta)
try:
    admin.site.register(Movie, MovieAdmin)
    admin.site.register(Category)
    admin.site.register(Episode)
except admin.sites.AlreadyRegistered:
    pass  