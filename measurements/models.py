# Django Modules
from django.db import models

# App Modules
from accounts.models import User


class Measurement(models.Model):
    """
    Measurement made to a patient
    """
    user = models.ForeignKey(User)
    gps = models.TextField(blank=True, null=True)
    bpm = models.IntegerField(blank=True, null=True)
    hr_max = models.IntegerField(blank=True, null=True)
    effort = models.IntegerField(blank=True, null=True)
    recovery = models.IntegerField(blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True, default=1)
    status = models.CharField(max_length=255, null=True, blank=True)
    details = models.TextField(blank=True, null=True)
    raw = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
