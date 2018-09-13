from django.db import models

class Data(models.Model):
	currency1 = models.CharField(max_length=3)
	currency2 = models.CharField(max_length=3)
	amount = models.IntegerField()
	date = models.DateField(default='2018-03-03')