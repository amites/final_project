# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-15 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0016_auto_20161013_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='workouttype',
            name='Workout_end',
            field=models.TimeField(blank=True, default='That one day'),
        ),
        migrations.AddField(
            model_name='workouttype',
            name='workout_start',
            field=models.DateTimeField(default='That one day'),
        ),
    ]
