# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-13 09:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20180713_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tradingteams',
            name='background',
        ),
    ]
