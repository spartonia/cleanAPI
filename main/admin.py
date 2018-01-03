from django.contrib import admin

from .models import Firm, BookableSlot, Service

admin.site.register(Firm)
admin.site.register(Service)
admin.site.register(BookableSlot)