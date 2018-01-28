from django.shortcuts import render

from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny, IsAdminUser

from booking.models import Booking
from booking.serializers import (
	BookingSerializer,
	BookingCreateSerializer
)

from permissions import IsOwnerOrAdmin


class BookingListView(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = BookingSerializer
	# permission_classes = [IsOwnerOrAdmin]
	# queryset = Booking.objects.all()

	def get_queryset(self):
		user = self.request.user
		if user.is_staff:
			qs = Booking.objects.all()
		else:
			qs = Booking.objects.filter(user=user)
		return qs


class BookingCreateView(generics.CreateAPIView):
	lookup_field = 'pk'
	serializer_class = BookingCreateSerializer
	permission_classes = [AllowAny]

	def preform_create(self, serializer):
		print(serializer)
		serializer.save(user=self.request.use)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class BookingRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	serializer_class = BookingSerializer
	permission_classes = [IsOwnerOrAdmin]
	queryset = Booking.objects.all()

	# def get_queryset(self):
		# user = self.request.user
		# if user.is_staff:
		# 	qs = Booking.objects.all()
		# else:
		# 	qs = Booking.objects.filter(user=user)
		# qs = Booking.objects.all()
		# return qs
