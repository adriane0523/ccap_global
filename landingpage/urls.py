from django.urls import path
from landingpage import views

urlpatterns = [
    path('', views.landingpage, name='landing_page'),
]