from django.db import models
from django.contrib.auth.models import User

class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_format = models.CharField(max_length=10, choices=[('nepali', 'Nepali'), ('english', 'English')])

    def __str__(self):
        return f"{self.user.username} - {self.date_format}"
    

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
