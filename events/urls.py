from django.urls import path
from events import views

urlpatterns = [
    path('', views.events, name='events'),
    path('<uuid>', views.events_index, name="events_index"),
]