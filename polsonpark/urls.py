from django.urls import path
from .views import (
		index_view, 
		reservation_view, 
		interiors_view,
		packages_view,
		areaguide_view,
		contactus_view,
	)

app_name='polsonpark'
urlpatterns=[
	path('', index_view, name='index-page'),
	path('reservations/', reservation_view, name='reservations-page'),
	path('interiors/', interiors_view, name='interiors-page'),
	path('packages/', packages_view, name='packages-page'),
	path('areaguide/', areaguide_view, name='areaguide-page'),
	path('contactus/', contactus_view, name='contactus-page'),

]