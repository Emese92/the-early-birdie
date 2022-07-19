from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Booking
from django.views.generic.base import TemplateView
from .forms import BookingForm 


class HomeTemplateView(TemplateView):
    template_name = 'index.html'


class MenuTemplateView(TemplateView):
    template_name = 'menu.html'


class BookingList(generic.ListView):
    model = Booking
    template_name = 'bookings.html'
    Booking.objects.values()


class AddBooking(generic.ListView):
    model = Booking
    template_name = 'add_new_booking.html'

    def get(self, request):
        return render(request, 'add_new_booking.html', {'form': BookingForm(),})

    def add(request):
        if request.method == "POST":
            name = request.POST['name']
            booked_date = request.POST['booked_date']
            booked_time = request.POST['booked_time']
            party_size = request.POST['party_size']
            extra_info = request.POST['extra_info']
            
        
        return render(request, 'bookings.html',{
            'name':name,
            'booked_date':booked_date,
            'booked_time':booked_time,
            'party_size':party_size,
            'extra_info':extra_info,
            })

    

