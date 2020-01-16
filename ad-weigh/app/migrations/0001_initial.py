# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-14 01:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='metric_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='metric_grouping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grouping_name', models.CharField(max_length=200)),
                ('grouping_description', models.CharField(max_length=1200)),
                ('enum_grouping_type', models.CharField(max_length=50)),
                ('normalized_table_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='metric_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50)),
                ('enum_datatype', models.CharField(max_length=50)),
                ('type_metric_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.metric_category')),
                ('type_metric_grouping', models.ManyToManyField(to='app.metric_grouping')),
            ],
        ),
        migrations.CreateModel(
            name='metric_value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when_metric_occurred', models.DateTimeField()),
                ('numeric_value', models.FloatField(default=0.0)),
                ('string_value', models.CharField(max_length=1000)),
                ('boolean_value', models.NullBooleanField()),
                ('is_rate', models.BooleanField(default=False)),
                ('notes', models.TextField()),
                ('value_metric_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.metric_type')),
            ],
        ),
    ]