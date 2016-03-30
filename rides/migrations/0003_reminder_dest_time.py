# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_auto_20160330_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='dest_time',
            field=models.CharField(default=datetime.datetime(2016, 3, 30, 17, 10, 48, 595000, tzinfo=utc), max_length=64),
            preserve_default=False,
        ),
    ]
