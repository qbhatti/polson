from django.db import models

# Create your models here.

class Room(models.Model):
	# each room must have a room number
	room_number = models.IntegerField(null=False, blank=False)

	# create choices for status of the room
	Available = 'Available'
	Reserved = 'Reserved'
	Occupied = 'Occupied'
	out_of_service = 'Out of Service'
	

	ROOM_STATUS_CHOICES = (
		(Available, 'Available'),
		(Reserved, 'Reserved'),
		(Occupied, 'Occupied'),
		(out_of_service, 'Out of Service'),
	)

	room_status = models.CharField(
		max_length=20,
		choices=ROOM_STATUS_CHOICES,
		default=Available,
	)

	notes = models.TextField(null=True, blank=True)

	def __str__(self):
		return f"Room {self.room_number}"
