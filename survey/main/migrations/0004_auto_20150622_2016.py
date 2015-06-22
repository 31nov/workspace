# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20150622_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('pic', models.ImageField(upload_to='user', blank=True, verbose_name='사진', default='emptyUser.png')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '세부정보',
                'verbose_name': '세부정보',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='userInfo',
            field=models.ForeignKey(to='main.UserInfo', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='file_image',
            field=models.ImageField(upload_to='img/%Y/%m', blank=True, verbose_name='이미지:', default='X'),
            preserve_default=True,
        ),
    ]
