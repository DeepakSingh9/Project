# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-17 08:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
