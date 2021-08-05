from django.contrib import admin

from shop.models import Item
from shop.models import Review

# admin.site.register(Item)


@admin.register(Item)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name", "price", "is_public", "created_at"]
    list_filter = ["is_public"]


@admin.register(Review)
class PostAdmin(admin.ModelAdmin):
    search_fields = ["item"]
    list_display = ["item", "message", "created_at"]
