from django.conf.urls import url

from booking.views import (
	BookingListView,
	BookingCreateView,
	BookingRudView,
)


urlpatterns = [
	url(r'^list/$', BookingListView.as_view(), name='bookig-list'),
	url(r'^create/$', BookingCreateView.as_view(), name='bookig-create'),
	url(r'^list/(?P<pk>\d+)/$', BookingRudView.as_view(), name='firm-rud'),
]   