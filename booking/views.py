from django.shortcuts import render, get_object_or_404
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
    Booking.objects.values()
    def get(self,request):
        return render(request, 'add_new_booking.html', {
        'form': BookingForm(),
    })



        # def get_bookings(self, **kwargs):
        #     context = super().get_bookings(**kwargs)
        #     context['booking_list'] = Booking.objects.all()
        #     return context
        # def get_queryset(self):
        #     self.booking = get_object_or_404(Booking, name=self.kwargs['booking'])
        #     return Booking.objects.filter(booking=self.booking)


