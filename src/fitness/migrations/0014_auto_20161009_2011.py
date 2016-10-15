# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-10 03:11
from __future__ import unicode_literals

from django.db import migrations, models
import fitness.myFields


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0013_auto_20161009_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days',
            name='day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], max_length=8),
        ),
        migrations.RemoveField(
            model_name='workouttype',
            name='days',
        ),
        migrations.AddField(
            model_name='workouttype',
            name='days',
            field=fitness.myFields.DayOfTheWeekField(choices=[(b'1', 'Monday'), (b'2', 'Tuesday'), (b'3', 'Wednesday'), (b'4', 'Thursday'), (b'5', 'Friday'), (b'6', 'Saturday'), (b'7', 'Sunday')], default=8, max_length=1),
        ),
    ]