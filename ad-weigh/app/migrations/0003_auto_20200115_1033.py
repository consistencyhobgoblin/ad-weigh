# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-15 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200114_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metric_value',
            name='when_metric_occurred',
        ),
        migrations.AddField(
            model_name='metric_value',
            name='when_metric_begin',
            field=models.DateTimeField(blank=True, null=True, verbose_name='metric begin date'),
        ),
        migrations.AddField(
            model_name='metric_value',
            name='when_metric_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='metric end date'),
        ),
        migrations.AlterField(
            model_name='metric_category',
            name='category_name',
            field=models.CharField(max_length=50, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='metric_category',
            name='normalized_table_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='datamart table'),
        ),
        migrations.AlterField(
            model_name='metric_type',
            name='enum_datatype',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='datatype'),
        ),
        migrations.AlterField(
            model_name='metric_type',
            name='type_metric_grouping',
            field=models.ManyToManyField(blank=True, to='app.metric_grouping'),
        ),
        migrations.AlterField(
            model_name='metric_type',
            name='type_name',
            field=models.CharField(max_length=50, verbose_name='metric type'),
        ),
        migrations.AlterField(
            model_name='metric_value',
            name='boolean_value',
            field=models.NullBooleanField(verbose_name='true-false value'),
        ),
        migrations.AlterField(
            model_name='metric_value',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='notes'),
        ),
        migrations.AlterField(
            model_name='metric_value',
            name='numeric_value',
            field=models.FloatField(default=0.0, verbose_name='number value'),
        ),
        migrations.AlterField(
            model_name='metric_value',
            name='string_value',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='text value'),
        ),
    ]
