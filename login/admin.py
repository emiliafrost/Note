from django.contrib import admin
from .import models
from booking import models as bookingmodels


class BookingsInline (admin.StackedInline):
    model = bookingmodels.Booking
    extra = 0


class UserAdmin (admin.ModelAdmin):
    model = models.User
    inlines = [BookingsInline]


# Register your models here.
admin.site.register(models.User, UserAdmin)