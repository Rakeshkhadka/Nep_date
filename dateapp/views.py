from django.shortcuts import render

# Create your views here.
# datedisplay/views.py
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .models import UserSettings, Event
from .serializer import EventSerializer
from rest_framework.response import Response
from nepali_datetime import date as nepali_date
from datetime import datetime
from rest_framework.viewsets import ModelViewSet

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = []
