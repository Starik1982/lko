# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-13 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentator', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('comments_text', models.TextField(blank=True, default=None, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comments_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Message')),
            ],
        ),
    ]
