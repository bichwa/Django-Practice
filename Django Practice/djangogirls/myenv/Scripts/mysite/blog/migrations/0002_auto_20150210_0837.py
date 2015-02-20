# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=datetime.datetime(2015, 2, 10, 8, 37, 12, 822000, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 10, 8, 36, 54, 980000, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
