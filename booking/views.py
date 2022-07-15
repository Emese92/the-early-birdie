from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Booking
from django.views.generic.base import TemplateView

class HomeTemplateView(TemplateView):
    template_name = 'index.html'

class MenuTemplateView(TemplateView):
    template_name = 'menu.html'


# class BookingList(generic.ListView):
#     model = Booking
#     queryset = Booking.objects.order_by('-booked_date') 
#     template_name = 'bookings.html'
#     paginate_by = 20


# class BookingDetail(View):
#     def get(self, request, slug, *args, **kwargs):
#         quesryset = Booking.objects.all()
#         booking = get_object_or_404(quesryset, slug=slug)
#         template_name = "booking_detail.html"
