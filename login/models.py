from django.db import models


# Create your models here.
class User(models.Model):
    # username should be unique, so we can figure out different users
    username = models.CharField(max_length=32, unique=True)  # 5-32
    name = models.CharField(max_length=64)
    homeAddress = models.CharField(max_length=128)
    password = models.CharField(max_length=256)  # 5-32, max_length=256 was assigned for safety
    phoneNo = models.CharField(max_length=16)
    email = models.EmailField(max_length=64)

    def __str__(self):
        return self.username
