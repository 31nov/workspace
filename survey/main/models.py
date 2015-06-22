from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    class Meta:
        verbose_name = u'프로필'
        verbose_name_plural = u'프로필'
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    nick = models.CharField(verbose_name=u'별명', max_length=50, blank=True,)
    pic = models.ImageField(verbose_name=u'사진', blank=True, default='emptyUser.png', upload_to='user')
#    
#    def __str__(self):
#        return ('user:%s, 이미지 파일-> %s') % (self.user.username, self.pic,)

class Article(models.Model):
    user = models.ForeignKey(User)
    
    title = models.CharField('글 제목', max_length=200)
    content = models.TextField('글 내용')
    written_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    file_image = models.ImageField('이미지:',blank=True, default='X', upload_to='img/%Y/%m')
    
    file_game_apk = models.FileField('게임 -> AOS :',blank=True, default='X')
    file_game_ios = models.FileField('게임 -> IOS :',blank=True, default='X')
    file_game_exe = models.FileField('게임 -> EXE :',blank=True, default='X')
    file_game_mac = models.FileField('게임 -> MAC :',blank=True, default='X')
    
    comment_count = models.IntegerField('댓글 수 ', default=0)
    like_count = models.IntegerField('좋아요 수', default=0)
    
    def __str__(self):
        return ('작성자: %s // 제목: %s //파일-> [img:%s], [apk:%s], [ios:%s], [exe:%s], [mac:%s]') % (self.user.username, self.title, self.file_image, self.file_game_apk, self.file_game_ios, self.file_game_exe, self.file_game_mac)

class Reply(models.Model):
    article = models.ForeignKey(Article)
    user = models.ForeignKey(User)
    
    comment = models.TextField('댓글 내용')
    written_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    file_image = models.FileField('이미지:',blank=True)
    
    def __str__(self):
        return ('글:%s 에 %s가 남긴 댓글, 파일-> %s') % (self.article.title, self.user.username, self.file_image,)

class Game(models.Model):
    game = models.CharField('title ',max_length=200)
    gameImage = models.CharField('img ',max_length=300)
    gameComment = models.CharField('comment 수 ', max_length=400, default=0)
    
    def __str__(self):
        return '%s : 이미지(%s)' % (self.game,self.gameImage,)