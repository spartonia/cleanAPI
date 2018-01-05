import datetime
from django.db import models

from rest_framework.reverse import reverse as api_reverse


class Firm(models.Model):
	org_number  = models.CharField(max_length=120, null=True, blank=True)
	name  = models.CharField(max_length=120, null=True, blank=True)
	email = models.EmailField()
	phone = models.CharField(max_length=15, null=True, blank=True)
	zipcode = models.CharField(max_length=15, null=True, blank=True)
	
	def __str__(self):
		return str(self.name)

	def get_api_url(self, request=None):
		return api_reverse('api-main:firm-retrieve', kwargs={'pk': self.pk}, 
			request=request)


class Service(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return str(self.name)


class BookableSlot(models.Model):
	firm = models.ForeignKey(Firm)
	service = models.ForeignKey(Service)
	date = models.DateField(default=datetime.datetime.now)
	price = models.IntegerField(default=40)

	def __str__(self):
		return str( "%s, %s, %s" % (self.firm, self.service, self.date))
