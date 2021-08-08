from django.contrib import admin
from movie.models import Actor, Movie, Video, Review


@admin.register(Actor)
class ActorAdmin((admin.ModelAdmin)):
    search_fields = ["name"]
    list_display = ["name", "photo"]


@admin.register(Movie)
class MovieAdmin((admin.ModelAdmin)):
    search_fields = ["title"]
    list_display = ["title", "poster", "actor", "desc"]


@admin.register(Video)
class VideoAdmin((admin.ModelAdmin)):
    search_fields = ["movie"]
    list_display = ["movie", "youtube_url"]


@admin.register(Review)
class ReviewAdmin((admin.ModelAdmin)):
    search_fields = ["movie"]
    list_display = ["movie", "message"]
