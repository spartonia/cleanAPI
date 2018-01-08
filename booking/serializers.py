from rest_framework import serializers

from booking.models import Booking


class BookingSerializer(serializers.ModelSerializer):
	"""Serializer for Booking class"""
	class Meta:
		model = Booking
		fields = [
			'id',
			'zipcode',
			'address',
			'area',
			'rut',
			'comment',
			'booking_slot',
		]
		read_only_field = ['id']

	def validate_zipcode(self, value):
		# TODO: update and repeat for other fields
		if len(value) < 5:
			raise serializers.ValidationError("Please provide a valid zipcode.")
		return value
