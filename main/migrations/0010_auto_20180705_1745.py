# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-05 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20180630_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logotip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_1', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('image_2', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('image_3', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('image_4', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('image_5', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('image_6', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('image_7', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('image_8', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('image_9', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
                ('image_10', models.ImageField(blank=True, default=None, null=True, upload_to='images/')),
            ],
        ),
        migrations.AddField(
            model_name='tradingteams',
            name='picture',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Logotip'),
        ),
    ]
