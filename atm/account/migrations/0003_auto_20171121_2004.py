# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20171121_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecash',
            name='balance',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='fund',
            name='balance_all',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='fund',
            name='last_year_balance',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='annuity',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dollar_balance',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='hk_balance',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='yuan_balance',
            field=models.CharField(max_length=200),
        ),
    ]