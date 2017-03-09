# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 21:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Edu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=64, verbose_name='school')),
                ('degree', models.CharField(max_length=32, verbose_name='degree')),
                ('field_of_study', models.CharField(max_length=64, verbose_name='field of study')),
                ('date_start', models.DateField(verbose_name='start date')),
                ('date_end', models.DateField(verbose_name='end date')),
                ('short_desc', models.CharField(max_length=128, verbose_name='short description')),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='title')),
                ('company', models.CharField(max_length=64, verbose_name='company')),
                ('location', models.CharField(max_length=64, verbose_name='location')),
                ('date_start', models.DateField(verbose_name='start date')),
                ('date_end', models.DateField(verbose_name='end date')),
                ('short_desc', models.CharField(max_length=128, verbose_name='short description')),
                ('description', models.TextField(verbose_name='description')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_addr', models.CharField(max_length=128, verbose_name='street address')),
                ('unit', models.CharField(max_length=8, verbose_name='unit')),
                ('city', models.CharField(max_length=64, verbose_name='city')),
                ('state', models.CharField(max_length=4, verbose_name='state')),
                ('post_code', models.CharField(max_length=5, verbose_name='postal code')),
                ('mobile', models.CharField(max_length=10, verbose_name='mobile')),
                ('email', models.CharField(max_length=64, verbose_name='email')),
                ('repo', models.CharField(max_length=64, verbose_name='repo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to='aboutme.Profile'),
        ),
        migrations.AddField(
            model_name='edu',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school', to='aboutme.Profile'),
        ),
    ]