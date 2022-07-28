from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
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
        context = {"form": form, }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.account = request.user
            form.save()
            messages.info(request, "Your booking is awaiting approval")
            return redirect('/bookings')
        context = {"form": form, }
        return render(request, self.template_name, context)


def editBooking(request, pk=None):
    booking = get_object_or_404(Booking, pk=pk)
    form = BookingForm(request.POST or None, request.FILES or None, instance=booking)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.instance.account = request.user
        form.save()
        messages.success(request, "Booking updated")
        return redirect('/bookings')

    context = {"form": form, }
    template = 'edit_booking.html'
    return render(request, template, context)


def deleteBooking(request, pk):

    booking = Booking.objects.get(pk=pk)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking deleted")
        return redirect('/bookings')
    return render(request, "delete.html")


class Confirmation(View):

    def post(self, request, slug, *args, **kwargs):
        booking = Booking.objects.get(slug=slug)
        if request.method == 'POST':
            booking.approved = not booking.approved
            booking.save()
            messages.success(request, "Booking confrimed")
            return redirect('/bookings')

        return render(request, 'bookings.html')
