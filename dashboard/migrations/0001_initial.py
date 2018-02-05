# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-13 04:19
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation_name', models.CharField(max_length=128)),
                ('organisation_description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=128, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,10}$')])),
                ('keyskills', models.CharField(blank=True, max_length=128, null=True)),
                ('profile_image', models.ImageField(blank=True, upload_to='profilepic/')),
            ],
        ),
    ]
