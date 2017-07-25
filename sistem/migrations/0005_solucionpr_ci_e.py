# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sistem', '0004_auto_20170720_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='solucionpr',
            name='ci_e',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
