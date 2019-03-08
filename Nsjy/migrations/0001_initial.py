# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dnum', models.CharField(max_length=20, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe7\xbc\x96\xe5\x8f\xb7')),
                ('dname', models.IntegerField(default=1, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe5\x93\x81\xe7\x89\x8c', choices=[(1, b'\xe8\x81\x94\xe6\x83\xb3\xef\xbc\x88Lenovo\xef\xbc\x89'), (2, b'\xe6\x88\xb4\xe5\xb0\x94\xef\xbc\x88Dell\xef\xbc\x89'), (3, b'\xe6\x83\xa0\xe6\x99\xae\xef\xbc\x88HP\xef\xbc\x89'), (4, b'\xe5\x85\x84\xe5\xbc\x9f\xef\xbc\x88Brother\xef\xbc\x89'), (5, b'\xe7\x90\x86\xe5\x85\x89')])),
                ('dtype', models.IntegerField(default=1, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba'), (2, b'\xe6\x89\x93\xe5\x8d\xb0\xe6\x9c\xba'), (3, b'\xe8\x87\xaa\xe5\xaa\x92\xe4\xbd\x93\xe8\xae\xbe\xe5\xa4\x87')])),
                ('cpname', models.CharField(max_length=20, verbose_name=b'\xe8\xae\xbe\xe5\xa4\x87\xe5\x90\x8d\xe7\xa7\xb0')),
                ('ip', models.GenericIPAddressField(protocol=b'ipv4', verbose_name=b'IP\xe5\x9c\xb0\xe5\x9d\x80')),
                ('mac', models.CharField(max_length=20, verbose_name=b'MAC\xe5\x9c\xb0\xe5\x9d\x80')),
                ('disk', models.CharField(max_length=50, verbose_name=b'\xe7\xa3\x81\xe7\x9b\x98\xe5\xba\x8f\xe5\x88\x97\xe5\x8f\xb7')),
                ('systype', models.IntegerField(default=1, verbose_name=b'\xe7\xb3\xbb\xe7\xbb\x9f\xe5\x9e\x8b\xe5\x8f\xb7', choices=[(1, b'win7-64'), (2, b'win7-32'), (3, b'winxp'), (4, b'win10-32'), (5, b'win10-64')])),
                ('dlocation', models.CharField(max_length=50, verbose_name=b'\xe7\x89\xa9\xe7\x90\x86\xe4\xbd\x8d\xe7\xbd\xae')),
                ('ctime', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['cpname'],
                'verbose_name': '\u8bbe\u5907\u4fe1\u606f',
                'verbose_name_plural': '\u8bbe\u5907\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flow', models.CharField(max_length=20, verbose_name=b'\xe6\xa5\xbc\xe5\xb1\x82')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postname', models.CharField(max_length=20, verbose_name=b'\xe7\xa7\x91\xe5\xae\xa4\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roomnum', models.CharField(max_length=4, verbose_name=b'\xe6\x88\xbf\xe9\x97\xb4\xe5\x8f\xb7')),
                ('function', models.CharField(max_length=10, verbose_name=b'\xe6\x88\xbf\xe9\x97\xb4\xe5\x8a\x9f\xe8\x83\xbd')),
                ('flow', models.ForeignKey(verbose_name=b'\xe6\xa5\xbc\xe5\xb1\x82', to='Nsjy.Flow')),
                ('postname', models.ForeignKey(verbose_name=b'\xe7\xa7\x91\xe5\xae\xa4\xe5\x90\x8d\xe7\xa7\xb0', to='Nsjy.Post')),
            ],
            options={
                'ordering': ['roomnum'],
                'verbose_name': '\u623f\u95f4\u4fe1\u606f',
                'verbose_name_plural': '\u623f\u95f4\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tname', models.CharField(max_length=20, verbose_name=b'\xe8\x80\x81\xe5\xb8\x88\xe5\x90\x8d\xe5\xad\x97')),
                ('sex', models.IntegerField(default=1, verbose_name=b'\xe8\x80\x81\xe5\xb8\x88\xe6\x80\xa7\xe5\x88\xab', choices=[(1, b'\xe7\x94\xb7'), (2, b'\xe5\xa5\xb3')])),
                ('tel', models.CharField(max_length=15, verbose_name=b'\xe8\x80\x81\xe5\xb8\x88\xe5\x8a\x9e\xe5\x85\xac\xe5\xae\xa4\xe7\x94\xb5\xe8\xaf\x9d')),
                ('phone', models.CharField(max_length=11, verbose_name=b'\xe8\x80\x81\xe5\xb8\x88\xe7\xa7\x81\xe4\xba\xba\xe7\x94\xb5\xe8\xaf\x9d')),
                ('room', models.ForeignKey(verbose_name=b'\xe6\x88\xbf\xe9\x97\xb4\xe5\x8f\xb7', to='Nsjy.Room')),
            ],
            options={
                'ordering': ['tname'],
                'verbose_name': '\u804c\u5de5\u4fe1\u606f',
                'verbose_name_plural': '\u804c\u5de5\u4fe1\u606f',
            },
        ),
        migrations.AddField(
            model_name='device',
            name='room',
            field=models.ForeignKey(verbose_name=b'\xe6\x88\xbf\xe9\x97\xb4\xe5\x8f\xb7', to='Nsjy.Room'),
        ),
    ]
