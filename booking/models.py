from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime as dt


class Booking(models.Model):
    slug = models.SlugField(max_length=200, unique=True, null=False)
    booked_date = models.DateField()
    booked_time = models.TimeField(default=dt.time(00, 00))
    name = models.CharField(max_length=200)
    party_size = models.PositiveSmallIntegerField(null=False)
    extra_info = models.TextField(blank=True)
    booked_on = models.DateTimeField(auto_now=True)
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings", null=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-booked_date']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

