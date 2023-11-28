from django.db import models


class History(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    request_text = models.TextField()

    def __str__(self):
        return f'{self.created_at} : {self.request_text}'
