from django.db import models
from tinymce.models import HTMLField
import uuid
from ckeditor_uploader.fields import RichTextUploadingField


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()  
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)


class Project_post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()  
    content = RichTextUploadingField()
    project = models.ForeignKey('Project',  on_delete=models.CASCADE )
    post_number = models.IntegerField(default=0)
