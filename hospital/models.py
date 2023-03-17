from django.db import models
from django import forms


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

class PersonData(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    birth_date = forms.DateField()
    height = forms.FloatField()
    weight = forms.FloatField()
    address = forms.CharField(widget=forms.Textarea)
    gender = forms.CharField(max_length=255)
    phone_number = forms.IntegerField()
    email_id = forms.EmailField()
    add_image = forms.ImageField(upload_to='./face_images/')