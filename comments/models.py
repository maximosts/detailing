# comments/models.py

from django.db import models
from django.conf import settings

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()  # Ensure this field exists
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
