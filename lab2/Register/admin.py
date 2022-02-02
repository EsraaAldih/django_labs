from django.contrib import admin
from .models import myuser 
from affairs.models import Track, Intake 


# Register your models here.
admin.site.register(myuser)
admin.site.register(Track)
admin.site.register(Intake)