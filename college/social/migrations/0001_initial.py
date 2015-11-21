# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('usertype', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('branch', models.CharField(max_length=10)),
            ],
        ),
    ]
