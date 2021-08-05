from django_proj2 import journal
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("journal/", include("journal.urls")),
]