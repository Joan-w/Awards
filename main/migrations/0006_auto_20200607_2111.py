# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-07 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200607_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
