from django.conf.urls import url

from main.views import (
	FirmAPIView, 
	FrimRetrieveView,
	ServiceAPIView,
	ServiceRetrieveView,
	BookableSlotAPIView,
	BookbleSlotRetrieveView,
)


urlpatterns = [
	url(r'^firm/$', FirmAPIView.as_view(), name='firm-list'),
	url(r'^firm/(?P<pk>\d+)/$', FrimRetrieveView.as_view(), name='firm-retrieve'),
	url(r'^service/$', ServiceAPIView.as_view(), name='service-list'),
	url(r'^service/(?P<pk>\d+)/$', ServiceRetrieveView.as_view(), name='service-retrieve'),
	url(r'^search/$', BookableSlotAPIView.as_view(), name='slot-list'),
	url(r'^search/(?P<pk>\d+)/$', BookbleSlotRetrieveView.as_view(), name='slot-retrieve'),
]   