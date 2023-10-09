import requests

from django.core.management.base import BaseCommand
from test_app import models


class Command(BaseCommand):
    help = 'Update currency and exchange'

    def handle(self, *args, **options):
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        response = requests.get(url)
        data = response.json()

        currencies = data['Valute']
        for currency_data in currencies.values():
            char_code = currency_data['CharCode']
            name = currency_data['Name']

            currency, created = models.Currency.objects.get_or_create(char_code=char_code)
            currency.name = name
            currency.save()

            exchange = models.Exchange.objects.create(currency=currency, date=data['Date'][:10],
                                                      value=currency_data['Value'])
            exchange.save()
