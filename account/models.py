from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	"""A user profile (booker)"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=15, blank=True, null=True)
