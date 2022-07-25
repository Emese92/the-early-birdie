from . import views
from django.urls import path
from .views import HomeTemplateView, MenuTemplateView, BookingList, AddBooking, post

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('menu/', MenuTemplateView.as_view(), name='menu'),
    path('bookings/', views.BookingList.as_view(), name='bookings'),
    path('add_new_booking/', AddBooking.as_view(), name='add_new_booking'),
    path('add_new/', post, name='add_new'),

]