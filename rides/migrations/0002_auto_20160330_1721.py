# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('src_lat', models.CharField(max_length=64)),
                ('src_lng', models.CharField(max_length=64)),
                ('dest_lat', models.CharField(max_length=64)),
                ('dest_lng', models.CharField(max_length=64)),
                ('reminder_time', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Remainder',
        ),
    ]
