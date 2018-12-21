from django.db import models
from login import models as loginmodels


# Create your models here.
class Booking(models.Model):
    username = models.ForeignKey(loginmodels.User, on_delete=models.CASCADE)
    numboxes = models.IntegerField('Number of boxes', default=0)
    Daddress = models.CharField('Destination address', max_length=128, default=' ')
    Paddress = models.CharField('Pick up address', max_length=128, default=' ')
    shipdate = models.CharField('Shipment date', max_length=128, default=' ')
    messages = models.CharField('Messages to Shipper', max_length=128, default=' ')
    crttime = models.DateTimeField('Create time', auto_now_add=True)

    def __str__(self):
        return self.username


