# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 16:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0014_auto_20161009_2011'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Days',
        ),
        migrations.RemoveField(
            model_name='workouttype',
            name='days',
        ),
    ]
