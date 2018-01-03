from django.test import TestCase

from .models import Firm


class FirmModelTestCase(TestCase):
	"""This class defines the test suit for the Firm model"""

	def setUp(self):
		"""Define int variables"""
		self.firm_name = "testFirm"
