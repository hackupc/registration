# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-09-21 14:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judging', '0006_auto_20181021_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentationevaluation',
            name='completion',
        ),
        migrations.AddField(
            model_name='presentationevaluation',
            name='idea',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presentationevaluation',
            name='smoke',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presentationevaluation',
            name='ux',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
            preserve_default=False,
        ),
    ]
