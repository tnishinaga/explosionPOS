# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20160420_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='code',
            field=models.IntegerField(default=0, verbose_name='JAN code'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='item_code',
            field=models.IntegerField(default=0, verbose_name='JAN code'),
        ),
    ]