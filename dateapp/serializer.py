from .models import Event
from rest_framework.serializers import ModelSerializer
from django.db import models

from config.fields import DateField, DateTimeField

class DateSerializer(ModelSerializer):
    serializer_field_mapping = {
        **ModelSerializer.serializer_field_mapping,
        models.DateField: DateField,
        models.DateTimeField: DateTimeField,
    }


class EventSerializer(DateSerializer):
    class Meta:
        model = Event
        fields = ['name', 'date']