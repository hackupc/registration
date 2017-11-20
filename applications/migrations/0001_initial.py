# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-11-01 23:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20171101_1602'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('submission_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status_update_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('R', 'Not accepted'), ('I', 'Invited'), ('LR', 'Last reminder'), ('C', 'Confirmed'), ('X', 'Cancelled'), ('A', 'Attended'), ('E', 'Expired')], default='P', max_length=2)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'Non-binary')], max_length=20, null=True)),
                ('under_age', models.BooleanField()),
                ('origin_city', models.CharField(max_length=300)),
                ('origin_country', models.CharField(max_length=300)),
                ('first_timer', models.BooleanField()),
                ('description', models.TextField(max_length=500)),
                ('projects', models.TextField(blank=True, max_length=500, null=True)),
                ('scholarship', models.BooleanField()),
                ('lennyface', models.CharField(default='-.-', max_length=300)),
                ('resume', models.FileField(upload_to='resumes')),
                ('authorized_privacy', models.BooleanField(default=False)),
                ('graduation_year', models.IntegerField(choices=[(2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021'), (2022, '2022')], default=2017)),
                ('university', models.CharField(max_length=300)),
                ('degree', models.CharField(max_length=300)),
                ('github', models.URLField(blank=True, null=True)),
                ('devpost', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('site', models.URLField(blank=True, null=True)),
                ('diet', models.CharField(choices=[('None', 'No requirements'), ('Vegeterian', 'Vegeterian'), ('Vegan', 'Vegan'), ('No pork', 'No pork'), ('Gluten-free', 'Gluten-free'), ('Others', 'Others')], default='None', max_length=300)),
                ('other_diet', models.CharField(blank=True, max_length=600, null=True)),
                ('tshirt_size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default='M', max_length=3)),
                ('team', models.BooleanField()),
                ('teammates', models.CharField(blank=True, max_length=300, null=True)),
                ('invited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invited_applications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]