# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='file_image',
            field=models.ImageField(verbose_name='이미지:', blank=True, default='X', upload_to='%Y/%m'),
            preserve_default=True,
        ),
    ]
