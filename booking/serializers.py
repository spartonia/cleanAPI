
from django.contrib.auth import get_user_model

from rest_framework import serializers

from booking.models import Booking
from main.models import BookableSlot

User = get_user_model()


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


class BookingCreateSerializer(serializers.ModelSerializer):
	"""Serializer for Booking class"""

	def __init__(self, *args, **kwargs):
		super(BookingCreateSerializer, self).__init__(*args, **kwargs)
		self.fields['booking_slot'].queryset = BookableSlot.objects.filter(
			booking__isnull=True)

	email = serializers.EmailField(write_only=True)
	name = serializers.CharField(write_only=True)
	personal_number = serializers.CharField(write_only=True)

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
			'personal_number',
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

	def create(self, validated_data):
		email = validated_data.pop('email')
		first_name = validated_data.pop('name')
		personal_number = validated_data.pop('personal_number')
		user_obj, created = User.objects.get_or_create(
			email=email
		)
		if created:
			user_obj.username = email
			user_obj.first_name = first_name
			user_obj.profile.personal_number = personal_number
			user_obj.save()
		# print(validated_data)
		booking = Booking(user=user_obj, **validated_data)
		booking.save()

		return booking
