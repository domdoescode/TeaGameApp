# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 10:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datastore', '0003_auto_20170531_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drinkrequirements',
            name='mug_clean',
        ),
    ]
