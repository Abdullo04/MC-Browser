# models.py
from django.db import models


class SearchHistory(models.Model):
    query = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    is_bookmarked = models.BooleanField(default=False)

    def __str__(self):
        return self.query
