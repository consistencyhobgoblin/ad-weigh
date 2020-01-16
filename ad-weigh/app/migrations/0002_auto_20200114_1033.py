# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-14 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metric_grouping',
            name='normalized_table_name',
        ),
        migrations.AddField(
            model_name='metric_category',
            name='normalized_table_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metric_grouping',
            name='grouping_description',
            field=models.CharField(blank=True, max_length=1200, null=True),
        ),
        migrations.AlterField(
            model_name='metric_type',
            name='enum_datatype',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='metric_type',
            name='type_metric_grouping',
            field=models.ManyToManyField(blank=True, null=True, to='app.metric_grouping'),
        ),
        migrations.AlterField(
            model_name='metric_value',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='metric_value',
            name='string_value',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='metric_value',
            name='when_metric_occurred',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]