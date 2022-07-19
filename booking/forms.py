from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booked_date', 'booked_time', 'name', 'party_size', 'extra_info', ]



