# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-29 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kilogram', '0004_auto_20170629_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='thumbnail_image',
        ),
        migrations.AddField(
            model_name='photo',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
