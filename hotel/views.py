from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Room
from .forms import RoomForm

# Create your views here.

def room_view(request):
	rooms = Room.objects.all().order_by('room_number')
	context = {
		'rooms': rooms
	}

	return render(request, 'hotel/rooms.html', context)

def room_details_view(request, id=id):
	room = get_object_or_404(Room, pk=id)

	context = {
		'room': room
	}

	return render(request, 'hotel/room_details.html', context)

def new_room_view(request):
	form = RoomForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('../')

	context = {
		'form': form
	}

	return render(request, 'hotel/new_room.html', context)

def room_update_view(request, id=id):
	obj = get_object_or_404(Room, id=id)
	form = RoomForm(request.POST or None, instance=obj)
	if form.is_valid():
		print(request.POST)
		form.save()
		return redirect('../')

	context = {
		'form': form
	}
	return render(request, "hotel/new_room.html", context)

def room_delete_view(request, id=id):
	room = get_object_or_404(Room, id=id)

	if request.method == 'POST':
		room.delete()
		return redirect('../../')

	context = {
		'room': room
	}

	return render(request, 'hotel/room_delete.html', context)

def room_availability(request):
	no_room_error=""
	rooms = Room.objects.filter(room_status='Available')

	# if no rooms are available
	if len(rooms)<=0: 
		no_room_error = "No rooms are availab  for selected dates."

	context = {
		'rooms': rooms,
		'error': no_room_error
	}

	return render(request, 'hotel/room_available.html', context)