# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistem', '0007_auto_20170721_0610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fluidos',
            name='adm',
        ),
        migrations.RemoveField(
            model_name='materiales',
            name='admm',
        ),
        migrations.DeleteModel(
            name='fluidos',
        ),
        migrations.DeleteModel(
            name='materiales',
        ),
    ]
