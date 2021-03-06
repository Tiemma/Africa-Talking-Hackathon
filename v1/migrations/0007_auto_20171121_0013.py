# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 00:13
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('v1', '0006_auto_20171117_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='tags',
        ),
        migrations.AddField(
            model_name='topic',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='Stage',
        ),
    ]
