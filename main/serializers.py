from rest_framework import serializers

from main.models import Firm, Service, BookableSlot


class FirmSerializer(serializers.ModelSerializer):
	url = serializers.SerializerMethodField(read_only=True)
	class Meta:
		model = Firm
		fields = [
			'id',
			'url',
			'name',
			'email',
			'phone',
			'zipcode',
			'org_number',
		]
		read_only_fields = ['id']

	def get_url(self, obj):
		request = self.context.get('request')
		return obj.get_api_url(request=request)

	def validate_org_number(self, value):
		qs = Firm.objects.filter(org_number__iexact=value)  # including instance
		if self.instance:
			qs = qs.exclude(pk=self.instane.pk)
		if qs.exists():
			serializers.ValidationError("Thos Org. number has already been used")
		return value


class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = [
			'id',
			'name',
		]
		read_only_fields = ['id']


class BookableSlotSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookableSlot
		fields = [
			'firm',
			'service',
			'date',
			'price',
		]
