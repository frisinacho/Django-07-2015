# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20150703_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(default=b'', null=True, blank=True, validators=[photos.validators.badwords_detector]),
        ),
        migrations.AlterField(
            model_name='photo',
            name='license',
            field=models.CharField(max_length=3, choices=[(b'QUE', b'Quentin Tarantino'), (b'DSH', b'Dr. Schutlz')]),
        ),
    ]
