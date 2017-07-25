# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistem', '0002_auto_20170714_0708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solucionex',
            old_name='cod_prueba',
            new_name='cod_solex',
        ),
        migrations.RemoveField(
            model_name='solucionex',
            name='cod_ex',
        ),
        migrations.AddField(
            model_name='preguntas',
            name='rc',
            field=models.CharField(max_length=10, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solucionex',
            name='cod_pru',
            field=models.ForeignKey(blank=True, null=True, to='sistem.prueba'),
        ),
        migrations.AlterField(
            model_name='solucionpr',
            name='respuesta',
            field=models.BooleanField(max_length=200),
        ),
    ]
