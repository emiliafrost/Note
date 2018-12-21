from django.urls import path
from . import views

app_name = 'bookingpart'
urlpatterns = [
    path('booking/', views.booking, name='booking'),
]