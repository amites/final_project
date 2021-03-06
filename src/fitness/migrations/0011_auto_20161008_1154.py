# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0010_userweight'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muscle_group', models.CharField(choices=[('Chest', 'Chest'), ('Back', 'Back'), ('Shoulders', 'Shoulders'), ('Abs', 'Abs'), ('Legs', 'Legs'), ('Arms', 'Arms'), ('Cardio', 'Cardio')], max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='human_height_ft',
            field=models.IntegerField(help_text='Enter height in feet'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='human_height_in',
            field=models.IntegerField(help_text='Enter height in inches'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='human_weight',
            field=models.FloatField(help_text='Enter weight in pounds'),
        ),
    ]
