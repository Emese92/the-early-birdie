from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('booked_date', 'booked_time', 'name', 'party_size', 'approved')
    search_fields = ['name', 'booked_date']
    list_filter = ('booked_on', 'approved')
    prepopulated_fields = {'slug': ('name', 'booked_date', 'booked_time',)}

    def approve_booking(self, request, queryset):
        queryset.update(approved=True)
