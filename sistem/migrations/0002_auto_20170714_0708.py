# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sistem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('usuario', models.CharField(max_length=40)),
                ('accion', models.CharField(max_length=40)),
                ('modulo', models.CharField(max_length=40)),
                ('sesion', models.CharField(max_length=40)),
                ('fecha_hora', models.DateTimeField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.RemoveField(
            model_name='bitacora',
            name='ci_u',
        ),
        migrations.AddField(
            model_name='prueba',
            name='activa',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='prueba',
            name='titulo',
            field=models.CharField(max_length=250, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fluidos',
            name='adm',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='materiales',
            name='admm',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='prueba',
            name='ci_p',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='solucionex',
            name='ci_e',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='bitacora',
        ),
        migrations.DeleteModel(
            name='usuario',
        ),
    ]
