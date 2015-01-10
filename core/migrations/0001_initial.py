# -*- coding: utf-8 -*-
# flake8: noqa
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aplicacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='data de modifica\xe7\xe3o', auto_now_add=True)),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servidor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='data de cria\xe7\xe3o')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='data de modifica\xe7\xe3o', auto_now_add=True)),
                ('name', models.CharField(max_length=25, verbose_name=b'hostname')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
