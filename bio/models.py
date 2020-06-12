from django.db import models

# Create your models here.
class Bio(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    bio = models.TextField()
    headshot = models.CharField(max_length=255)
    board = models.BooleanField(default=False)