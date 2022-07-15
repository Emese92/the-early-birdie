from . import views
from django.urls import path
from .views import HomeTemplateView, MenuTemplateView


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('menu/', MenuTemplateView.as_view(), name='menu'),
    # path('bookings/', views.BookingList.as_view(), name='booking'),
    # path('<slug:slug>', views.BookingDetail),
    
]