# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170619_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='current_address',
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
