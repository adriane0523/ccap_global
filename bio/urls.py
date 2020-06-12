from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='bio'),
    path('<uuid>/', views.projects_index, name=""),
]