import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.postgres.fields import HStoreField

# Create your models here.

class Room(models.Model):
	# each room must have a room number
	room_number = models.IntegerField(null=False, blank=False, unique=True)

	notes = models.TextField(null=True, blank=True)

	rate = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return f"Room {self.room_number}"

	def save(self, *args, **kwargs):

		# if new room is created
		if self.pk == None:

			#get last record with date less than or equal to today
			last_entry = DailyActivity.objects.filter(date__lte=timezone.now().date()).latest('date')
			print(last_entry)
			# if last_entry date is not for today, fill in the blanks till today
			days_missing = timezone.now().date() - last_entry.date
			print(days_missing)
			if (days_missing > timedelta(days=0)):
				last_date = last_entry.date
				while(last_date < timezone.now().date()):
					print("in while loop***********************************")
					new_day = DailyActivity.objects.create(date=(last_date+timedelta(days=1)), room_statuses=last_entry.room_statuses)
					new_day.save()
					last_date = last_date + timedelta(days=1)

			#else if last_entry date is today's date, add this room_number to room room_statuses to today and all days following today
			future_entries = DailyActivity.objects.filter(date__gte=timezone.now().date())
			for day in future_entries:
				print("in for loop**************************************")
				statuses = day.room_statuses
				statuses[self.room_number] = 'a'
				day.room_statuses = statuses
				day.save()
		
		super().save(*args, **kwargs)




	def display_furniture(self):
		"generate a string of all the furniture items in a room"
		return ', '.join(furniture.item_name for furniture in self.furniture_set.all())
	
	display_furniture.short_description = 'Furniture'

	@property
	def number_of_people(self):
		count = 0
		furniture_items = self.furniture_set.all()
		for furniture in furniture_items:
			if furniture.sleepable:
				count += furniture.number_it_sleeps
		return count

class Furniture(models.Model):
	"""model to add available furniture"""
	
	item_name = models.CharField(max_length=120, unique=True)
	sleepable = models.BooleanField(default=False)
	number_it_sleeps = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)], blank=True, null=True)
	description = models.TextField(null=True, blank=True)
	rooms = models.ManyToManyField(Room)

	def __str__(self):
		return f"{self.item_name}"

	def display_rooms(self):
		"""generate string of all the rooms that a furniture item is in."""
		return ', '.join(str(room.room_number) for room in self.rooms.all())

	display_rooms.short_description = 'Rooms'

class Guest(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return f"{self.name}"

class Reservation(models.Model):
	room_reserved = models.ManyToManyField(Room)
	guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
	in_date = models.DateField()
	out_date = models.DateField()
	res_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

	def __str__(self):
		return f"Room: {self.room_reserved}, Check In: {self.in_date}, Check Out: {self.out_date}, Booked by: {self.guest}"


class DailyActivity(models.Model):
	date = models.DateField()
	room_statuses = HStoreField()

	def __str__(self):
		return f"{self.date}"

	def save(self, *args, **kwargs):
		if self.pk == None:
			latest_entry = DailyActivity.objects.latest('date')

			# if current entry is more than one day in advance of latest entry, add missing dates
			missing_days = self.date - latest_entry.date - timedelta(days=1) # timedelta between consecutive dates is 1
			count = 1
			while(missing_days > timedelta(days=0)):
				new_entry = DailyActivity.objects.create(date=(latest_entry.date+timedelta(days=count)), room_statuses=latest_entry.room_statuses)
				new_entry.save()
				missing_days = missing_days - timedelta(days=1)
				count += 1

		super().save(*args, **kwargs)

