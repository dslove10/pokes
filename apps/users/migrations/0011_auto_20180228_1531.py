# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-28 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_user_pokes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poke',
            name='pokes',
        ),
        migrations.AddField(
            model_name='user',
            name='pokes',
            field=models.IntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='poke',
            name='poked_by',
        ),
        migrations.AddField(
            model_name='poke',
            name='poked_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='poked_me', to='users.User'),
            preserve_default=False,
        ),
    ]
