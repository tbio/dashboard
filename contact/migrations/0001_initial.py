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
            name='Conversation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('seen', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_deleted', models.DateTimeField(null=True, blank=True)),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='conversation_receiver')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='conversation_sender')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('message', models.CharField(max_length=10000)),
                ('seen', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('deleted', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_deleted', models.DateTimeField(null=True, blank=True)),
                ('conversation', models.ForeignKey(to='contact.Conversation', related_name='conversation')),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='message_receiver')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='message_sender')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
