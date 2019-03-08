# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nsjy', '0004_teacher_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='sex',
        ),
    ]
