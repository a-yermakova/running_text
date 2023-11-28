from django.db import models


class History(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    request_url = models.TextField()
