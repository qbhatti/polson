from django.contrib import admin
from .models import Room, Furniture, Guest, Reservation, DailyActivity
# Register your models here.

class FurnitureInline(admin.TabularInline):
    model = Furniture.rooms.through

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
	model = Room
	inlines = [
			FurnitureInline,
		]
	list_display = ('room_number', 'rate', 'display_furniture', 'number_of_people')

	class Meta:
		model = Room

@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
	list_display = ('item_name', 'sleepable', 'display_rooms')
	fields = ('item_name', 'sleepable', 'number_it_sleeps', 'description')
	inlines = [
			FurnitureInline,
		]
	class Meta:
		model = Furniture

@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
	pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	pass

@admin.register(DailyActivity)
class DailyActivityAdmin(admin.ModelAdmin):
	pass