from .models import Booking
from django import forms
import datetime as dt


# TIME_CHOICES = [(i, dt.time(i).strftime('%I:%M %p')) for i in range(6, 11)]
PARTY_SIZE = [(i, i) for i in range(1, 11)]

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = [
            'booked_date',
            'booked_time',
            'name',
            'party_size',
            'extra_info',
        ]
        widgets = {
            'booked_date': forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={'type': 'date'}),
            'booked_time': forms.TimeInput(attrs={'type': 'time'}),
            'party_size': forms.Select(choices=PARTY_SIZE),
            'extra_info': forms.widgets.Textarea(
                attrs={"placeholder": "Food allergies, dietary requirements, special occasions...", })
        }

