# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-28 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20171117_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(default='not sure', max_length=50),
        ),
    ]
