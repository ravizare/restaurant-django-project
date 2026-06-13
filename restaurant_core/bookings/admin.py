from django.contrib import admin
from .models import MenuItem, Booking # Make sure Booking is imported

admin.site.register(MenuItem)
admin.site.register(Booking) # Register the booking model here
