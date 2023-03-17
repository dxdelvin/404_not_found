from django.contrib import admin
from . import models

# Register your models here.


class PersonDataAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','username','birth_date','height','weight','address','gender',
                    'phone_number','email_id')


admin.site.register(models.PersonData, PersonDataAdmin)
