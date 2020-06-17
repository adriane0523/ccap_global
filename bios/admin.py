from django.contrib import admin

# Register your models here.
from bios.models import Bio

class BioAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bio, BioAdmin)