# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-11 13:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_tradingteams_brands_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logotip',
            name='image_10',
        ),
        migrations.RemoveField(
            model_name='logotip',
            name='image_11',
        ),
        migrations.RemoveField(
            model_name='logotip',
            name='image_12',
        ),
    ]