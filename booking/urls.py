from django.urls import path
from . import views

app_name = 'bookingpart'
urlpatterns = [
    path('bookings/', views.bookings, name='bookings'),
]