# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20180614_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default=12345, max_length=15),
            preserve_default=False,
        ),
    ]