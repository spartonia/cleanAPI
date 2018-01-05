from django.shortcuts import render

from rest_framework import generics, mixins

from booking.models import Booking
from booking.serializers import BookingSerializer
from booking.permissions import IsOwnerOrAdmin


class BookingListView(generics.ListAPIView):
# class BookingAPIView(generics.ListAPIView):
	# TODO: add permissions. Only user can view its listings or an admin
	lookup_field = 'pk'
	serializer_class = BookingSerializer

	def get_queryset(self):
		user = self.request.user
		if user.is_staff:
			qs = Booking.objects.all()
		else:
			qs = Booking.objects.filter(user=user)
		return qs


class BookingCreateView(generics.CreateAPIView):
	lookup_field = 'pk'
	serializer_class = BookingSerializer
	# permission_classes = []

	def preform_create(self, serializer):
		serializer.save(user=self.request.user)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class BookingRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = BookingSerializer
	permission_classes = [IsOwnerOrAdmin]
	# queryset = Booking.objects.all()

	def get_queryset(self):
		# user = self.request.user
		# if user.is_staff:
		# 	qs = Booking.objects.all()
		# else:
		# 	qs = Booking.objects.filter(user=user)
		qs = Booking.objects.all()
		return qs
