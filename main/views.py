from django.shortcuts import render
from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.permissions import (
	AllowAny,
	IsAdminUser,
	IsAuthenticated,
	IsAuthenticatedOrReadOnly,
)

from main.models import Firm, Service, BookableSlot
from main.serializers import ( 
	FirmSerializer, 
	ServiceSerializer, 
	BookableSlotSerializer
)
from permissions import (
	IsAdminOrReadOnly,
	IsOwnerOrReadOnly
)


# class FirmAPIView(mixins.CreateModelmixin, generics.ListAPIView):
class FirmAPIView(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = FirmSerializer
	permission_classes = [IsAdminOrReadOnly]

	# queryset = Firm.objects.all()
	
	def get_queryset(self):
		qs = Firm.objects.all()
		query = self.request.GET.get('q')
		if query is not None:
			qs = qs.filter(
				Q(org_number__iexact=query)|
				Q(phone__icontains=query)  # TODO: updade with suitable filter
			).distinct()

		return qs

	def get_serializer_context(self, *args, **kwargs):
		return {'request': self.request}


class FrimRetrieveView(generics.RetrieveAPIView):
	lookup_field = 'pk'
	serializer_class = FirmSerializer
	permission_classes = [IsAdminOrReadOnly]
	queryset = Firm.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {'request': self.request}

	# def get_object(self):
	# 	pk = self.kwargs.get('pk')
	# 	return Firm.objects(pk=pk)
	# 	


class ServiceAPIView(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = ServiceSerializer
	queryset = Service.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {'request': self.request}


class ServiceRetrieveView(generics.RetrieveAPIView):
	lookup_field = 'pk'
	serializer_class = ServiceSerializer
	# permission_classes = [IsOwnerOrReadOnly]
	queryset = Service.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {'request': self.request}


class BookableSlotAPIView(generics.ListAPIView):
	lookup_field = 'pk'
	serializer_class = BookableSlotSerializer
	permission_classes = [IsAdminOrReadOnly]

	def get_queryset(self):
		qs = BookableSlot.objects.filter(
			booking__isnull=True)
		return qs

	def get_serializer_context(self, *args, **kwargs):
		return {'request': self.request}


class BookbleSlotRetrieveView(generics.RetrieveAPIView):
	lookup_field = 'pk'
	serializer_class = BookableSlotSerializer
	permission_classes = [IsAdminOrReadOnly]
	queryset = BookableSlot.objects.all()

	def get_serializer_context(self, *args, **kwargs):
		return {'request': self.request}