from django.shortcuts import render
from .models import Room
# Create your views here.

def room_view(request):
	rooms = Room.objects.all()
	context = {
		'rooms': rooms
	}

	return render(request, 'hotel/rooms.html', context)

def room_details_view(request, room_number):
	room = Room.objects.get(room_number=room_number)
	
	context = {
		'room': room
	}

	return render(request, 'hotel/room_details.html', context)
