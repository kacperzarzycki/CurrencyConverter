from django.db import models
from django import forms
from .models import Data

class DataForm(forms.ModelForm):
	class Meta:
		model = Data
		fields = ('currency1', 'currency2', 'amount', 'date') 