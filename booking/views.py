from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking


class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter(account=account).order_by('-booked_date') 
    template_name = 'bookings.html'
    paginate_by = 20

 


class BookingDetail(View):

    def get(self, request, slug, *args, **kwargs):
        quesryset = Booking.objects.all()
        booking = get_object_or_404(quesryset, slug=slug)

    return render(
        request,
        "booking_detail.html",)