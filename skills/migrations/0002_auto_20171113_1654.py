# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-13 11:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bio',
            name='profile',
        ),
        migrations.AddField(
            model_name='bio',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
