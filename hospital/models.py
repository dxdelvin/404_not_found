from django.db import models


# Create your models here.

class PersonData(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    birth_date = models.DateField()
    height = models.FloatField()
    weight = models.FloatField()
    address = models.CharField(max_length=1000)
    gender = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    email_id = models.CharField(max_length=255)
    add_image = models.ImageField(upload_to='./face_images/')

