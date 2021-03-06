from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField()

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    poster = models.ImageField()
    desc = models.TextField()

    def __str__(self) -> str:
        return self.title


class Video(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    youtube_url = models.URLField()


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    message = models.TextField()
