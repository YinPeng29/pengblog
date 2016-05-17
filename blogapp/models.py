#-*-coding:utf-8-*-

from django.db import models

# Create your models here.

class Publishers(models.Model):
    '''
    出版社集
    '''
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Authors(models.Model):
    '''
    书籍作者集
    '''
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True,verbose_name='e-mail')

    def __str__(self):
        return u'%s %s'%(self.first_name,self.last_name)

class Books(models.Model):
    '''
    推荐书籍
    导航栏中展示
    '''
    title = models.CharField(max_length=100,verbose_name=u'书名')
    author = models.ManyToManyField(Authors,verbose_name=u'作者')
    publisher = models.ForeignKey(Publishers,verbose_name=u'出版社')
    book_pub_date = models.DateTimeField(blank=True,null=True,verbose_name=u'出版日期')

    def __str__(self):
        return self.title

class Life_notes(models.Model):
    '''
    生活笔记
    导航栏中展示
    '''
    title = models.CharField(max_length=100,verbose_name=u'题目')
    content = models.TextField(verbose_name=u'文章内容')
    note_pub_date = models.DateTimeField(blank=True,null=True,verbose_name=u'发布日期')

class Actors(models.Model):
    '''
    演员集
    '''
    name = models.CharField(max_length=50,verbose_name=u'演员姓名')
    genter = models.CharField(max_length=30,verbose_name=u'性别')
    birthday = models.DateField(blank=True,null=True,verbose_name=u'生日')
    tall = models.IntegerField(verbose_name=u'身高')

class Directors(models.Model):
    name = models.CharField(max_length=50,verbose_name=u'导演姓名')
    genter = models.CharField(max_length=30,verbose_name=u'性别')

class Movies(models.Model):
    '''
    电影
    导航栏中展示
    '''
    name = models.CharField(max_length=50,verbose_name=u'电影名称')
    actor = models.ManyToManyField(Actors,verbose_name=u'演员')
    derector = models.ForeignKey(Directors,verbose_name=u'导演')
    movie_length = models.IntegerField(verbose_name=u'时长(分钟)')
    show_time = models.DateTimeField(verbose_name=u'上映时间')

class Program_notes(models.Model):
    '''
    编程笔记(教程)
    导航栏中展示
    '''
    pro_type = models.OneToOneField(Programs,verbose_name=u'笔记类型')
    pro_title = models.CharField(max_length=100,verbose_name=u'标题')
    content = models.TextField(verbose_name=u'内容')
    pro_pub_date = models.DateTimeField(blank=True,null=True,verbose_name=u'发布日期')

class Programs(models.Model):
    '''
    编程语
    '''
    pro_name = models.CharField(max_length=50,verbose_name=u'语言')
    creater = models.CharField(max_length=50,verbose_name=u'创始人')
    create_date = models.DateTimeField(blank=True,null=True,verbose_name=u'创始时间')

