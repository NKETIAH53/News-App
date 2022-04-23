from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("daily_news:detail", kwargs={"id": self.id})
    
    def __str__(self):
        return self.title