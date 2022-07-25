from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, FormView
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


# class AddBooking(CreateView):
#     model = Booking
#     template_name = 'add_new_booking.html'
#     fields = [
#             'booked_date',
#             'booked_time',
#             'name',
#             'party_size',
#             'extra_info',
#         ]

#     def get(self, request):
#         form = BookingForm()
#         return render(request, 'add_new_booking.html', {"form": form})



#     def add(request, *args, **kwargs):
#         if request.method == 'POST':
#             self.object.create(booked_date=booked_date,
#                 booked_time=booked_time,
#                 name=name,
#                 party_size=party_size,
#                 extra_info=extra_info,)
#             return redirect(get)


#         return render(request, "add_new_booking.html")

class AddBooking(CreateView):
    model = Booking
    form = BookingForm()
    template_name = 'add_new_booking.html'
    
    def get(self, request):
        form = BookingForm()
        return render(request, 'add_new_booking.html', {"form": form})

def post(self, request, *args, **kwargs):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        booking = BookingForm.save(commit=False)
        booking.save()

    return render(request)

