# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0008_auto_20171121_0050'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='github_username',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='topic',
            name='twitter_username',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
