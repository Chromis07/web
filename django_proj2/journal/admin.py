from django.contrib import admin
from journal.models import Journalist, Post, Comment


@admin.register(Journalist)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "created_at", "updated_at"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["photo", "title", "content", "journalist", "created_at"]


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["post"]
    list_display = ["post", "message", "created_at", "updated_at"]
