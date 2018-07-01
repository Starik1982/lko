# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-30 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20180630_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('structural_unit', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('name_vacancy', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='VacancyBerezan',
        ),
        migrations.DeleteModel(
            name='VacancyKiev',
        ),
        migrations.DeleteModel(
            name='VacancyNivki',
        ),
        migrations.DeleteModel(
            name='VacancyOblast',
        ),
        migrations.DeleteModel(
            name='VacancyZhitomir',
        ),
    ]