from django.contrib import admin

# Register your models here.
from landingpage.models import Video

class VideoAdmin(admin.ModelAdmin):
    pass





admin.site.register(Video, VideoAdmin)
