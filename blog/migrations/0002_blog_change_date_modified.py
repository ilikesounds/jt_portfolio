# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 00:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_blog_init'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_modified',
            field=models.DateTimeField(blank=True, verbose_name='Date Modified'),
        ),
    ]
