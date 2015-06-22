# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20150622_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.ImageField(upload_to='user', verbose_name='사진', blank=True, default='emptyUser.png'),
            preserve_default=True,
        ),
    ]
