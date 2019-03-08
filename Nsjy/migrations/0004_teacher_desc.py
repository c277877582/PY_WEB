# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nsjy', '0003_auto_20181203_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='desc',
            field=models.CharField(default=b'', max_length=30, verbose_name=b'\xe8\x81\x8c\xe5\x8a\xa1'),
        ),
    ]
