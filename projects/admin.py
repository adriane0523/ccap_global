from django.contrib import admin

# Register your models here.
from projects.models import Project, Project_post

class ProjectAdmin(admin.ModelAdmin):
    pass

class Project_postAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project_post, Project_postAdmin)
admin.site.register(Project, ProjectAdmin)
