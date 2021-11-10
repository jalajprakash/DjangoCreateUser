from django.db import models

class Contact(models.Model):
    username = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=300)
    pincode = models.CharField(max_length=6)
    mobile = models.CharField(max_length=10 , unique=True)
