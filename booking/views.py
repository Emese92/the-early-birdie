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


def updateView(request):

    obj = get_object_or_404(Booking, slug=slug, user=request.user)
    form = BookingForm(request.POST, instance=obj)
    if form.is_valid():
        form.save()
    context = {"form": form, "booked": True, "confirmed": False, }
    return render(request, "edit_booking.html", context)


def deleteBooking(request, pk=None):

    booking = get_object_or_404(Booking, pk=pk)
    booking.delete()
    messages.success(request, "Booking Deleted")
    context = {"deleted": True,}
    return render(request, "delete.html", context)

# class UpdateBooking(UpdateView):
#     model = Booking
#     template_name = 'edit_booking.html'
#     fields = [
#             'booked_date',
#             'booked_time',
#             'name',
#             'party_size',
#             'extra_info',
#         ]
    # def edit(self, request, pk):
    #     booking = get_object_or_404(Booking)
    #     form = BookingForm(instance=booking)

    #     if request.method == POST:
    #         form = BookingForm(request.POST, instance=booking)
    #         if form.is_valid():
    #             form.instance.account = request.user
    #             form.save()
            
    #     context = {"form": form, "booked": True, "confirmed": False, }
    #     return render(request, self.template_name, context)

# def updateBooking(request, pk):
#     template_name = 'edit_booking.html'
#     booking = Booking.objects.get(id=pk)
#     form = BookingForm(instance=booking)
#     context = {"form": form}
#     return render(request, 'edit_booking.html', context)

# def deleteBooking(request):

#     form = BookingForm()
#     if request.method == POST:
#         booking.delete()
#     return redirect('bookings.html')