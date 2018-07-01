# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-30 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20180630_1614'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacancyBerezan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_vacancy', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VacancyKiev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_vacancy', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VacancyNivki',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_vacancy', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VacancyOblast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_vacancy', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VacancyZhitomir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_vacancy', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Vacancy',
        ),
    ]
