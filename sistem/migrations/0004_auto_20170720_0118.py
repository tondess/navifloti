# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistem', '0003_auto_20170719_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solucionex',
            name='Duracion',
        ),
        migrations.RemoveField(
            model_name='solucionex',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='solucionex',
            name='hora',
        ),
        migrations.RemoveField(
            model_name='solucionex',
            name='ponderacion',
        ),
        migrations.RemoveField(
            model_name='solucionex',
            name='seccion',
        ),
        migrations.AlterField(
            model_name='solucionpr',
            name='respuesta',
            field=models.CharField(max_length=10),
        ),
    ]
