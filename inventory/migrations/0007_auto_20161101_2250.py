# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160803171240 on 2016-11-01 21:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_auto_20161101_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration_owner',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Team', to_field='name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
