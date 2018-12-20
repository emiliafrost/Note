from django.db import models
from login import models as loginmodels


# Create your models here.
class Booking(models.Model):
    username = models.ForeignKey(loginmodels.User, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)

    def __str__(self):
        return self.content