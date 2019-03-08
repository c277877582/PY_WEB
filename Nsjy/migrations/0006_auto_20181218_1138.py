# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nsjy', '0005_remove_teacher_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='teacher',
            field=models.ForeignKey(default=b'', verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xba\xba', to='Nsjy.Teacher'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(max_length=11, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='room',
            field=models.ForeignKey(verbose_name=b'\xe6\x88\xbf\xe5\x8f\xb7', to='Nsjy.Room'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='tel',
            field=models.CharField(max_length=15, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='tname',
            field=models.CharField(max_length=20, verbose_name=b'\xe8\x81\x8c\xe5\x91\x98'),
        ),
    ]
