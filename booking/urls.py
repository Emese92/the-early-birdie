from . import views
from django.urls import path
from .views import HomeTemplateView


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    # path('bookings/', views.BookingList.as_view(), name='booking'),
    # path('<slug:slug>', views.BookingDetail),
    
]