# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('description', models.TextField(null=True, blank=True)),
                ('status', models.CharField(null=True, blank=True, max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_create')),
                ('measurement', models.ForeignKey(blank=True, null=True, to='measurements.Measurement')),
                ('patient', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='patient_history')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('status', models.CharField(null=True, blank=True, max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('relatives', models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='relatives_patient')),
                ('specialist', models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL, blank=True, related_name='specialist_patient')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
