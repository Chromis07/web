from django.db import models
from django.db.models.fields import BooleanField


class Item(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField()
    price = models.PositiveIntegerField()
    is_public = BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
