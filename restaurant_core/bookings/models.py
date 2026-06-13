from django.db import models  # <-- MAKE SURE THIS LINE IS AT THE VERY TOP!

class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name = models.CharField(max_length=200)
    guest_count = models.IntegerField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reservation for {self.customer_name}"
