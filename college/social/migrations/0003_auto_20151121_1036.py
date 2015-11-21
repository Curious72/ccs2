# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_remove_users_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='announcements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=10000)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='assignments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('text', models.FileField(upload_to=b'')),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='complaints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=10000)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='curriculum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=10000)),
                ('time', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='branch',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
