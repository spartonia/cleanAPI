import datetime

from django.conf import settings
from django.db import models


from main.models import BookableSlot


class Booking(models.Model):
	# TODO: Update user field on submit and create a new profile, if the user is not signed in.
	# TODO: Extend user (one-to_one) to have a profile w/ other info
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	zipcode = models.CharField(max_length=15)
	address = models.CharField(max_length=50)
	area = models.PositiveIntegerField()
	rut = models.BooleanField(default=True)
	comment = models.TextField(blank=True, null=True)

	# TDOD: auto comlete following fields bsed on fields above
	# total = .. (take into account the RUT etc)

	booking_slot = models.OneToOneField(
		BookableSlot, on_delete=models.CASCADE)

	def __str__(self):
		return str("%s, %s" % (self.zipcode, self.area))

	def get_serializer_context(self):
		return {'request': self.request}
