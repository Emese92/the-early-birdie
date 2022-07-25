from .models import Booking
from django import forms
import datetime as dt


TIME_CHOICES = [(i, dt.time(i).strftime('%I:%M %p')) for i in range(11)]

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
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                }),
            'booked_time': forms.Select(choices=TIME_CHOICES),
            
        }






