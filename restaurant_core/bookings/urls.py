from django.urls import path
from . import views

urlpatterns = [
    # Changing 'menu/' to '' makes this your main landing page
    path('', views.menu_view, name='booking_menu'), 
]
