# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170619_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='blood_group',
        ),
    ]