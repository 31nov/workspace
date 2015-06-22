# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20150622_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(verbose_name='사진', upload_to='user', blank=True, default='emptyUser.png'),
            preserve_default=True,
        ),
    ]
