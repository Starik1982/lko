# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-14 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='текст повідомлення'),
        ),
    ]
