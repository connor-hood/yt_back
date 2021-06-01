from django.db import models


# Create your models here.
class Comment(models.Model):
    user = models.CharField(max_length=50)
    comment = models.TextField(max_length=300)
    video_id = models.CharField(max_length=200)

# add models.SlugField() or models.UUIDField()?
