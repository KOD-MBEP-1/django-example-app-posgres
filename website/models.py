from django.db import models

# Create your models here.
class Movie (models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(max_length=200)
    seen = models.BooleanField(default=False)
    liked = models.BooleanField(default=False)
    def __str__(self):
        return self.title