from .models import Booking
from django import forms
import datetime as dt

# [(i, dt.time(i).strftime('%I:%M %p')) for i in range(6, 11)]
# TimeInput(attrs={'type': 'time','step':"300"}),
# TIME_CHOICES = (
#     ('1', '6:00'),
#     ('2', '6:30'),
#     ('3', '7:00'),
#     ('4', '7:30'),
#     ('5', '8:00'),
#     ('6', '8:30'),
#     ('7', '9:00'),
#     ('8', '9:30'),
#     ('9', '10:00'),
#     ('10', '10:30'),
#     ('11', '11:00'),   
# )
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
            'booked_time': 'Please input time between 6AM-11AM',
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

