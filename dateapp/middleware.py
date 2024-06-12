from .models import UserSettings
from django.utils.deprecation import MiddlewareMixin

class UserSettingsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:

            try:
                user_settings = UserSettings.objects.get(user=request.user)
                request.date_format = user_settings.date_format
            except UserSettings.DoesNotExist:
                request.date_format = 'english'
        else:
            request.date_format = 'english'
