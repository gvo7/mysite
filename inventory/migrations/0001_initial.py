# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration_owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('teamleader', models.CharField(max_length=50)),
                ('sdo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assettag', models.CharField(max_length=20)),
                ('hostname', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=50)),
                ('management_ipv4', models.GenericIPAddressField()),
                ('management_ipv6', models.GenericIPAddressField(blank=True, null=True)),
                ('os_version', models.CharField(max_length=20)),
                ('configuration_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Configuration_owner')),
            ],
        ),
        migrations.CreateModel(
            name='Integrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email_support', models.EmailField(max_length=254)),
                ('account_manager', models.CharField(max_length=100)),
                ('email_account_manager', models.EmailField(max_length=254)),
                ('service_manager', models.CharField(max_length=100)),
                ('email_service_manager', models.EmailField(max_length=254)),
                ('contract_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('eos_date', models.DateField(blank=True, null=True)),
                ('eol_date', models.DateField(blank=True, null=True)),
                ('logging_template', models.CharField(max_length=500)),
                ('monitoring_template', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email_support', models.EmailField(max_length=254)),
                ('account_manager', models.CharField(max_length=100)),
                ('email_account_manager', models.EmailField(max_length=254)),
                ('service_manager', models.CharField(max_length=100)),
                ('email_service_manager', models.EmailField(max_length=254)),
                ('contract_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Vendor'),
        ),
        migrations.AddField(
            model_name='device',
            name='integrator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Integrator'),
        ),
        migrations.AddField(
            model_name='device',
            name='management_interface',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Management'),
        ),
        migrations.AddField(
            model_name='device',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Product'),
        ),
        migrations.AddField(
            model_name='device',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Vendor'),
        ),
    ]
