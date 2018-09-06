from django.shortcuts import render
from currency_converter import CurrencyConverter
from datetime import date

cc = CurrencyConverter()

def index(request):
	currency_date = date(2018, 3, 20)
	first_currency = 'EUR'
	second_currency = 'PLN'
	amount = 785
	converted_amount = round(cc.convert(amount, first_currency, second_currency, date=currency_date), 3)
	context = {'first_currency': first_currency, 'second_currency': second_currency, 'amount': amount, 'converted_amount': converted_amount, 'currency_date': currency_date}
	return render(request, 'converter/index.html', context)
