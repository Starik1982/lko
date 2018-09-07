# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-13 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_delete_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]