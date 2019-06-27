from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
	notes = forms.CharField(
				required=False, 
				widget=forms.Textarea(attrs={
					'rows': 4,
					'cols': 50,
				}))

	class Meta:
		model = Room

		fields = [
			'room_number',
			'rate',
			'notes',
		]