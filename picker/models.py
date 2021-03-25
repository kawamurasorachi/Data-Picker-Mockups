from django.db import models
from django.conf import settings

class Topic(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CrawledData(models.Model):
    target = models.ForeignKey(
        Topic,
        blank=True, null=True,
        on_delete=models.SET_NULL
    )
    url = models.URLField()
    title = models.CharField(max_length=100)
    description = models.TextField()

