# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sistem', '0005_solucionpr_ci_e'),
    ]

    operations = [
        migrations.CreateModel(
            name='nota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nota', models.IntegerField()),
                ('fecha', models.DateField()),
                ('ci_e', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('cod_p', models.ForeignKey(blank=True, null=True, to='sistem.prueba')),
            ],
        ),
    ]
