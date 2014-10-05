from django.contrib import admin
from .models import Patient, ClinicHistory

admin.site.register(Patient)
admin.site.register(ClinicHistory)
