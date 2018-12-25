from django.contrib import admin
from . import models


class AckInline (admin.StackedInline):
    model = models.Ack
    extra = 0


class Bookingadmin(admin.ModelAdmin):
    list_display = ('username', 'messages', 'crttime')
    model = models.Booking
    inlines = [AckInline]


# Register your models here.
admin.site.register(models.Booking, Bookingadmin)
