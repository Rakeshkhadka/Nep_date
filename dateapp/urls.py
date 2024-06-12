# datedisplay/urls.py
from django.urls import path
from .views import EventViewSet

urlpatterns = [
    path('events/', EventViewSet.as_view({'get': 'list', 'post': 'create'}), name='events'),
]
