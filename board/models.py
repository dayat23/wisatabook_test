from django.db import models


class BookStore(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    short_summary = models.TextField(null=True, blank=True, db_index=True)
    published_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
