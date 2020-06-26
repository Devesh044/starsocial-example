# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-22 17:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 17, 48, 24, 972829, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 17, 48, 24, 971831, tzinfo=utc)),
        ),
    ]
