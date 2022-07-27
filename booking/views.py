from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, FormView, UpdateView
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
        context = {"form": form, "booked": False, "confirmed": False, "deleted": False, }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.account = request.user
            form.save()
        
        context = {"form": form, "booked": True, "confirmed": False, "deleted": False,}
        return render(request, self.template_name, context)


def editBooking(request, pk=None):
    booking = get_object_or_404(Booking, pk = pk)
    form = BookingForm(request.POST or None, request.FILES or None, instance=booking)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Post updated") 
        return HttpResponseRedirect('bookings.html')
        form.instance.account = request.user
        form.save()

    context = {"form": form, "booked": True, "confirmed": False, "deleted": False,}
    template = 'edit_booking.html'
    return render(request, template, context)



def deleteBooking(request, pk=None):

    booking = get_object_or_404(Booking, pk=pk)
    booking.delete()
    messages.success(request, "Booking Deleted")
    context = {"deleted": True,}
    return render(request, "delete.html", context)

