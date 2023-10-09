from django.shortcuts import render
from .models import Exchange


def show_rates(request):
    date = request.GET.get('date')
    exchange_rates = Exchange.objects.filter(date=date)
    print(exchange_rates)
    return render(request, 'show_rates.html', {'exchange_rates': exchange_rates})

