# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numbas_lti', '0007_auto_20160616_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ltiuserdata',
            name='lis_outcome_service_url',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='ltiuserdata',
            name='lis_result_sourcedid',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
