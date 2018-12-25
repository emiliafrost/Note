from django.urls import path
from . import views

app_name = 'bookingpart'
urlpatterns = [
    path('bookings/', views.bookings, name='bookings'),
    path('bookings/create/', views.create, name='create'),
    path('bookings/<int:booking_id>/', views.details, name='details'),
    path('ack/', views.ack, name='ack')
]