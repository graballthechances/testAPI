# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 13:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0009_auto_20171122_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='up',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yuan_balance', models.CharField(default='100', max_length=200)),
                ('dollar_balance', models.CharField(default='100', max_length=200)),
                ('hk_balance', models.CharField(default='100', max_length=200)),
                ('annuity', models.CharField(default='100', max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='up', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]