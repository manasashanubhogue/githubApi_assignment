# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_search', '0002_auto_20171003_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
