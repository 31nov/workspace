# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='글 제목', max_length=200)),
                ('content', models.TextField(verbose_name='글 내용')),
                ('written_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('file_image', models.FileField(blank=True, default='X', verbose_name='이미지:', upload_to='')),
                ('file_game_apk', models.FileField(blank=True, default='X', verbose_name='게임 -> AOS :', upload_to='')),
                ('file_game_ios', models.FileField(blank=True, default='X', verbose_name='게임 -> IOS :', upload_to='')),
                ('file_game_exe', models.FileField(blank=True, default='X', verbose_name='게임 -> EXE :', upload_to='')),
                ('file_game_mac', models.FileField(blank=True, default='X', verbose_name='게임 -> MAC :', upload_to='')),
                ('comment_count', models.IntegerField(default=0, verbose_name='댓글 수 ')),
                ('like_count', models.IntegerField(default=0, verbose_name='좋아요 수')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('game', models.CharField(verbose_name='title ', max_length=200)),
                ('gameImage', models.CharField(verbose_name='img ', max_length=300)),
                ('gameComment', models.CharField(default=0, verbose_name='comment 수 ', max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('comment', models.TextField(verbose_name='댓글 내용')),
                ('written_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('file_image', models.FileField(blank=True, verbose_name='이미지:', upload_to='')),
                ('article', models.ForeignKey(to='main.Article')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('pic', models.FileField(blank=True, default='media/user/emptyIser.png', verbose_name='사진', upload_to='')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '세부정보',
                'verbose_name_plural': '세부정보',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='userInfo',
            field=models.ForeignKey(to='main.UserInfo'),
            preserve_default=True,
        ),
    ]
