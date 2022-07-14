from django.shortcuts import render
from django.views import generic
from .models import Booking


class BookingList(genericView):
    model = Booking
    queryset = Booking.objects.order_by('-booked_date') 
    template_name = 'bookings.html'
    paginate_by = 20