from django.urls import path
from .views import (
		room_view,
		room_details_view,
		new_room_view,
		room_update_view,
		room_delete_view,
		room_availability,
	)

app_name='hotel'
urlpatterns=[
	path('', room_view, name='room-page'),
	path('new/', new_room_view, name='new-room-page'),
	path('available/', room_availability, name='rooms-available'),
	path('<int:id>/', room_details_view, name='room-details-page'),
	path('<int:id>/update/', room_update_view, name='room-update-page'),
	path('<int:id>/delete/', room_delete_view, name='room-delete-page'),
]