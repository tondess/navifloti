# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistem', '0006_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='nota',
            field=models.CharField(max_length=10),
        ),
    ]
