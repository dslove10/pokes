# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_poke_poked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poke',
            name='poked_by',
        ),
        migrations.RemoveField(
            model_name='poke',
            name='users',
        ),
        migrations.AddField(
            model_name='user',
            name='pokes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Poke',
        ),
    ]
