# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-07 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200607_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.URLField(default=None, null=True),
        ),
    ]
