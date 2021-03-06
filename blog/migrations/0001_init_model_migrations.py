# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 21:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aboutme', '0001_init_model_migrations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('date_created', models.DateTimeField(verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(blank=True, null=True, verbose_name='Date Modified')),
                ('published_status', models.CharField(choices=[('Prv', 'Private'), ('Pub', 'Public')], default='Prv', max_length=3, verbose_name='Published Status')),
                ('body', models.TextField(verbose_name='Body')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='aboutme.Profile')),
            ],
        ),
    ]
