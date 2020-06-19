from django.urls import path
from projects import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<uuid>/', views.project_posts, name="project_posts"),
    path('<uuid>/<int:index>', views.projects_index, name="projects_index"),
]