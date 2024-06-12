from rest_framework import serializers
from nepali_datetime import date as nepali_date, datetime as nepali_datetime

class DateField(serializers.DateField):
    def to_representation(self, value):
        request = self.context.get('request', None)
        if request and request.date_format == 'nepali':
            nep_date = nepali_date.from_datetime_date(value)
            return str(nep_date)
        return super().to_representation(value)

    def to_internal_value(self, data):
        request = self.context.get('request', None)
        if request and request.date_format == 'nepali':
            #expected data 2078-01-01
            nepali_date_parts = [int(part) for part in data.split('-')]
            nepalidate = nepali_date(*nepali_date_parts)
            greg_date = nepalidate.to_datetime_date()
            print(greg_date)
            return greg_date
        return super().to_internal_value(data)


class DateTimeField(serializers.DateTimeField):
    def to_representation(self, value):
        request = self.context.get('request', None)
        if request and request.date_format == 'nepali':
            nep_datetime = nepali_datetime.from_datetime_datetime(value)
            return str(nep_datetime)
        return super().to_representation(value)

    def to_internal_value(self, data):
        request = self.context.get('request', None)
        if request and request.date_format == 'nepali':
            #expected data 2078-01-01T12:00:00
            nepali_date_part, nepali_time_part = data.split('T')
            nepali_date_parts = [int(part) for part in nepali_date_part.split('-')]
            nepali_time_parts = [int(part) for part in nepali_time_part.split(':')]

            nepali_dt = nepali_datetime(
                nepali_date_parts[0],
                nepali_date_parts[1],
                nepali_date_parts[2],
                nepali_time_parts[0],
                nepali_time_parts[1],
                nepali_time_parts[2]
            )
            return nepali_dt.to_datetime_datetime()
        return super().to_internal_value(data)
