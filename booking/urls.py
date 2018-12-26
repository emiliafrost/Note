from django.urls import path
from . import views

app_name = 'bookingpart'
urlpatterns = [
    path('bookings/', views.bookings, name='bookings'),
    path('bookings/create/', views.create, name='create'),
    path('bookings/<int:booking_id>/', views.details, name='details'),
    path('bookings/ack/', views.ack, name='ack'),
    path('bookings/ack/<int:booking_id>/', views.ackdetail, name='ack-detail')
]