from django.db import models
import uuid

# Create your models here.
class Bio(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    startdate = models.CharField(max_length=255)
    enddate = models.CharField(max_length=255)
    bio = models.TextField()
    headshot = models.ImageField(upload_to='headshot/')
    board = models.BooleanField(default=False)
    past = models.BooleanField(default=False)
    bid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)