# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specialist', '0001_initial'),
        ('auth', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='institute',
            field=models.ForeignKey(related_name='institute_user', blank=True, null=True, default=None, to='specialist.Institute'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(help_text='Specific permissions for this user.', related_query_name='user', blank=True, verbose_name='user permissions', to='auth.Permission', related_name='user_set'),
            preserve_default=True,
        ),
    ]
