# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-10-13 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judging', '0007_auto_20190921_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
