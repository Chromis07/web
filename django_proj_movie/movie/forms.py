from django import forms
from movie.models import Actor, Review, Movie


class ActorForm(forms.ActorForm):
    class Meta:
        model = Actor
        fields = ["name", "photo"]


class MovieForm(forms.MovieForm):
    class Meta:
        model = Movie
        fields = ["title", "poster", "actor", "desc"]


class ReviewForm(forms ReviewForm):
    class Meta:
        model = Review
        fields = ["movie", "message"]
