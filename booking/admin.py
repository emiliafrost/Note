from django.contrib import admin
from . import models


class Bookingadmin(admin.ModelAdmin):
    list_display = ( 'username', 'messages', 'crttime')


# Register your models here.
admin.site.register(models.Booking, Bookingadmin)
