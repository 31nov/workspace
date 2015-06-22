# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150622_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='article',
            name='userInfo',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
