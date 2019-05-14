from django.urls import path
from .views import (
		room_view,
		room_details_view,
	)

app_name='hotel'
urlpatterns=[
	path('', room_view, name='room-page'),
	path('<int:room_number>/', room_details_view, name='room-details-page'),
]