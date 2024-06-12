from django.contrib import admin
from .models import UserSettings, Event
# Register your models here.

admin.site.register([UserSettings, Event])
