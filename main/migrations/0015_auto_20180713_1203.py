# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-13 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20180711_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('name', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('description', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tradingteams',
            name='brands_logo',
        ),
        migrations.DeleteModel(
            name='Logotip',
        ),
    ]
