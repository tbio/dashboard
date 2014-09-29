# Django Modules
from django.db import models

# App Modules
from accounts.models import User
from measurements.models import Measurement


class Patient(models.Model):
    """
    User Profile
    """
    user = models.OneToOneField(User)
    relatives = models.ManyToManyField(User, related_name='relatives_patient', blank=True, null=True)
    specialist = models.ManyToManyField(User, related_name='specialist_patient', blank=True, null=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


class ClinicHistory(models.Model):
    """
    Clinic History
    """
    patient = models.ForeignKey(User, related_name='patient_history')
    created_by = models.ForeignKey(User, related_name='user_create')
    description = models.TextField(blank=True, null=True)
    measurement = models.ForeignKey(Measurement, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
