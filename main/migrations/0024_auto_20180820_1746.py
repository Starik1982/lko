# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-20 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_delete_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comments_message',
        ),
        migrations.AddField(
            model_name='message',
            name='comments_message',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='main.Comments'),
            preserve_default=False,
        ),
    ]
