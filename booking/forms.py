from .models import Booking
from django import forms

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

        help_texts = {
            'booked_time': 'Please input time between 6am-11am',
        }
        widgets = {
            'booked_date': forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={'type': 'date'}),
            'booked_time': forms.TimeInput(attrs={'type': 'time', 'min': '06:00', 'max': '11:00'}),
            'party_size': forms.Select(choices=PARTY_SIZE),
            'extra_info': forms.widgets.Textarea(
                attrs={"placeholder": "Food allergies, dietary requirements, special occasions...", })
        }
