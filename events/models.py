from django.db import models
from tinymce.models import HTMLField
import uuid
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()  
    content = RichTextUploadingField()
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

   

   