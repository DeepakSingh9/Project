# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-15 04:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0003_auto_20171114_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='cert_image',
            field=models.FileField(blank=True, upload_to='cert_images/'),
        ),
        migrations.AlterField(
            model_name='certification',
            name='year',
            field=models.DateField(),
        ),
    ]
