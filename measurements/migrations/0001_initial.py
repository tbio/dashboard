# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('gps', models.TextField(null=True, blank=True)),
                ('bpm', models.IntegerField(null=True, blank=True)),
                ('hr_max', models.IntegerField(null=True, blank=True)),
                ('effort', models.IntegerField(null=True, blank=True)),
                ('recovery', models.IntegerField(null=True, blank=True)),
                ('interval', models.IntegerField(null=True, blank=True, default=1)),
                ('status', models.CharField(null=True, blank=True, max_length=255)),
                ('details', models.TextField(null=True, blank=True)),
                ('raw', models.TextField(null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
