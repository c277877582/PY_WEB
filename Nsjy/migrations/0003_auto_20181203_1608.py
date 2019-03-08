# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nsjy', '0002_auto_20181203_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='roomnum',
            field=models.CharField(max_length=5, verbose_name=b'\xe6\x88\xbf\xe9\x97\xb4\xe5\x8f\xb7'),
        ),
    ]
