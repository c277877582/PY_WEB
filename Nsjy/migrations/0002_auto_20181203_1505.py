# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nsjy', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flow',
            options={'verbose_name': '\u697c\u5c42\u4fe1\u606f', 'verbose_name_plural': '\u697c\u5c42\u4fe1\u606f'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': '\u79d1\u5ba4\u4fe1\u606f', 'verbose_name_plural': '\u79d1\u5ba4\u4fe1\u606f'},
        ),
    ]
