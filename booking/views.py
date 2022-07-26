from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, FormView
from .models import Booking
from django.views.generic.base import TemplateView
from .forms import BookingForm 
from django.contrib import messages


class HomeTemplateView(TemplateView):
    template_name = 'index.html'


class MenuTemplateView(TemplateView):
    template_name = 'menu.html'


class BookingList(generic.ListView):
    model = Booking
    template_name = 'bookings.html'
    Booking.objects.values()



class AddBooking(TemplateView):
    model = Booking
    form = BookingForm()
    template_name = 'add_new_booking.html'
    
    def get(self, request, *args, **kwargs):
        form = BookingForm()
        context = {"form": form, "booked": False, "confirmed": False,}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.account = request.user
            form.save()
        
        context = {"form": form, "booked": True, "confirmed": False,}
        return render(request, self.template_name, context)

