from django.db import models
from django.core.validators import MinLengthValidator


class Journalist(models.Model):
    name = models.CharField(
        max_length=20, db_index=True, validators=[MinLengthValidator(3)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    journalist = models.ForeignKey(Journalist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
