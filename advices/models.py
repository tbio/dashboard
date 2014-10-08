# Django Modules
from django.db import models

# App Modules
from accounts.models import User


class TipCategory(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=220, null=True, blank=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)


class Tip(models.Model):
    title = models.CharField(max_length=5000, blank=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User)
    category = models.ForeignKey(TipCategory, blank=True, null=True)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
