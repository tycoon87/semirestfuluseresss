# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-16 00:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='User',
        ),
    ]
