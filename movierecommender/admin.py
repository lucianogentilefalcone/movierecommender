from django.contrib import admin

# Register your models here.

from .models import Movie
from movierecommender.models import Movie


@admin.action(description="Update to watched movie")
def make_watched(modeladmin, request, queryset):
    queryset.update(watched = True)



class MovieAdmin(admin.ModelAdmin):
    fields = ['imdb_id', 'genres', 'original_title', 'overview', 'watched','vote_average']
    list_display = ('original_title', 'genres', 'release_date', 'watched','vote_average')
    search_fields = ['original_title', 'overview']
    actions = [make_watched]

admin.site.register(Movie, MovieAdmin)




