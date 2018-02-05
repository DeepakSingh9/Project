# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-16 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0002_auto_20171116_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Postings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(blank=True, max_length=128, null=True)),
                ('no_of_positions', models.IntegerField()),
                ('location', models.CharField(blank=True, max_length=128, null=True)),
                ('salary_range', models.CharField(blank=True, max_length=128, null=True)),
                ('requirements', models.TextField()),
                ('description', models.TextField()),
                ('posted_on', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobboard.Category')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Organization_Profile')),
            ],
        ),
    ]
