from django.db import models


# Create your models here.
class Comment(models.Model):
    user = models.CharField(max_length=50)
    comment = models.TextField(max_length=300)

# add models.SlugField() or models.UUIDField()?
