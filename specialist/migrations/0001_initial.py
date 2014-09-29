# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(null=True, blank=True, max_length=1000)),
                ('genre', models.CharField(null=True, blank=True, max_length=2)),
                ('address', models.CharField(null=True, blank=True, max_length=200)),
                ('website', models.CharField(null=True, blank=True, max_length=200)),
                ('zip_code', models.CharField(null=True, blank=True, max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('city', models.ForeignKey(blank=True, null=True, to='accounts.City')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('specialities', models.CharField(max_length=10000)),
                ('rate', models.IntegerField(null=True, blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('institute', models.ForeignKey(related_name='specialist_institute', blank=True, null=True, default=None, to='specialist.Institute')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='specialist_user')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(null=True, blank=True, max_length=1000)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
