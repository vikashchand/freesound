# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-28 14:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0010_auto_20170712_1537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='soundlicensehistory',
            options={'ordering': ('-created',)},
        ),
    ]
