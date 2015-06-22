# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150622_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='userInfo',
        ),
    ]
