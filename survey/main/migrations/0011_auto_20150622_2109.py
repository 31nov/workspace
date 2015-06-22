# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20150622_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='main/media/user/emptyUser.png', verbose_name='사진', upload_to='user', blank=True),
            preserve_default=True,
        ),
    ]
