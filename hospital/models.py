from django.db import models
from django import forms


class PersonData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255)
    birth_date = models.DateField(default="2003-09-08")
    height = models.FloatField(null=False, default=0)
    weight = models.FloatField(null=False, default=0)
    password = models.CharField(max_length=20, default=1234)
    address = models.CharField(max_length=1000)
    gender = models.CharField(max_length=255)
    phone_number = models.IntegerField(null=False, default=0)
    email_id = models.EmailField()
    add_image = models.ImageField(upload_to='./face_images/')
