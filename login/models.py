from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=128)
    # username should be unique, so we can figure out different users
    username = models.CharField(max_length=128, unique=True)
    homeAddress = models.CharField(max_length=128)
    password = models.CharField(max_length=256)
    phoneNo = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.username
