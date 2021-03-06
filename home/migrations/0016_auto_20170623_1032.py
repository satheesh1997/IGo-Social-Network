# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 10:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20170623_0539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='feed',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AlterField(
            model_name='like',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Feeds'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
