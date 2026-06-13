from django.shortcuts import render, redirect
from .models import MenuItem
from .forms import BookingForm # Import your brand new form file

def menu_view(request):
    # Fetch menu items
    items = MenuItem.objects.all()
    
    # Check if a customer just submitted a booking
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save() # Saves the reservation straight to the database!
            return redirect('booking_menu') # Refresh page cleanly after submission
    else:
        form = BookingForm() # Show a blank form on page load

    context = {
        'menu_items': items,
        'booking_form': form
    }
    return render(request, 'bookings/menu.html', context)
