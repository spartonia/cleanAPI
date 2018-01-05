
from django.contrib.auth import get_user_model

from rest_framework import serializers

from booking.models import Booking

User = get_user_model()


class BookingSerializer(serializers.ModelSerializer):
	"""Serializer for Booking class"""
	class Meta:
		model = Booking
		fields = [
			'id',
			'user',
			'zipcode',
			'address',
			'area',
			'rut',
			'comment',
			'booking_slot',
		]
		read_only_field = ['id']


class BookingCreateSerializer(serializers.ModelSerializer):
	"""Serializer for Booking class"""
	email = serializers.EmailField(write_only=True)
	name = serializers.CharField(write_only=True)

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
			'email',
			'name',
		]
		read_only_field = ['id']
		# extra_kwargs = {''}

	# def get_email(self, obj):
	# 	request = self.context.get('request')
	# 	return request.user.email

	def validate_zipcode(self, value):
		# TODO: update and repeat for other fields
		if len(value) < 5:
			raise serializers.ValidationError("Please provide a valid zipcode.")
		return value

	def create(self, validated_date):
		# TODO: create/update a Profile object
		# person, created = Person.objects.get_or_create(identifier=id)
		email=validated_date.pop('email')
		first_name=validated_date.pop('name')
		user_obj, created = User.objects.get_or_create(
			email=email
		)
		if created:
			user_obj.username = email
			user_obj.first_name = first_name
			user_obj.save()

		booking = Booking(**validated_date, user=user_obj)
		booking.save()

		return booking
