# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 01:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
