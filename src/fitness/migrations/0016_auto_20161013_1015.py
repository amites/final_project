# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 17:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0015_auto_20161011_0926'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='UserBMIProfile',
        ),
    ]