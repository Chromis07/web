from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField()

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=30)
    poster = models.ImageField()
    desc = models.TextField()

    def __str__(self) -> str:
        return self.name


class Video(models.Model):
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    youtube_url = models.URLField()

    def __str__(self) -> str:
        return self.name


class Review(models.Model):
    movie_name = models.ForeignKey(Movie, on_delete=models.CASCADE)
    message = models.TextField()
