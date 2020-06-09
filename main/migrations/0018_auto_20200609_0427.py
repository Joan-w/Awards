# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-09 01:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20200608_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='project',
            name='reviewDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 9, 1, 27, 55, 899053, tzinfo=utc)),
        ),
    ]