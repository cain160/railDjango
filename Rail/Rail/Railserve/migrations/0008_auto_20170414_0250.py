# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-14 02:50
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Railserve', '0007_auto_20170413_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='device',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True,
                                    to='Railserve.Position'),
        ),
    ]
