from django.contrib import admin
from .models import Architect, Building # import the Artist model from models.py
# Register your models here.


# Register your models here.

admin.site.register(Architect) # this line will add the model to the admin panel
admin.site.register(Building)