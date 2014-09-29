# Django Modules
from django.db import models

# App Modules
from accounts.models import User, City


class Speciality(models.Model):
    """
    Speciality
    """
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return self.user.name


class Institute(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    genre = models.CharField(max_length=2, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    city = models.ForeignKey(City, null=True, blank=True)
    zip_code = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return self.name


class Specialist(models.Model):
    """
    Trainer Profile
    """
    user = models.OneToOneField(User, related_name='specialist_user')
    specialities = models.CharField(max_length=10000, null=False, blank=False)
    institute = models.ForeignKey(Institute, related_name='specialist_institute', null=True, blank=True, default=None)
    rate = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return self.user.username
