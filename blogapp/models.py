#-*-coding:utf-8-*-

from django.db import models

# Create your models here.

class Publisher(models.Model):
    '''
    出版社集
    '''
    name = models.CharField(max_length=50,verbose_name=u'出版社')
    address = models.CharField(max_length=100,verbose_name=u'地址')
    city = models.CharField(max_length=100,verbose_name=u'所在城市')
    state_province = models.CharField(max_length=50,verbose_name=u'所在省份')
    country = models.CharField(max_length=50,verbose_name=u'国家')
    website = models.URLField(verbose_name=u'网址')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural=u'出版社'
        ordering = ['name']

class Author(models.Model):
    '''
    书籍作者集
    '''
    first_name = models.CharField(max_length=50,verbose_name=u'姓')
    last_name = models.CharField(max_length=50,verbose_name=u'名')
    # author_img = models.ImageField(upload_to='photos/authors',verbose_name=u'作者写真')   #添加作者写真
    author_info = models.TextField(verbose_name=u'作者简介')
    email = models.EmailField(blank=True,verbose_name='e-mail')

    def __str__(self):
        return u'%s %s'%(self.first_name,self.last_name)

    class Meta:
        verbose_name_plural=u'作者'

class Book(models.Model):
    '''
    推荐书籍
    导航栏中展示
    '''
    title = models.CharField(max_length=100,verbose_name=u'书名')
    book_img = models.ImageField(upload_to='photos/books',verbose_name=u'封面')   #添加书封面字段 2016/5/18
    author = models.ManyToManyField(Author,verbose_name=u'作者')
    book_intro = models.TextField(verbose_name=u'书籍简介')             #添加书籍简介  2016/5/18
    publisher = models.ForeignKey(Publisher,verbose_name=u'出版社')
    book_pub_date = models.DateTimeField(blank=True,null=True,verbose_name=u'出版日期')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural=u'书籍'
        ordering = ['title']

class Life_note(models.Model):
    '''
    生活笔记
    导航栏中展示
    '''
    title = models.CharField(max_length=100,verbose_name=u'题目')
    content = models.TextField(verbose_name=u'文章内容')
    note_pub_date = models.DateTimeField(blank=True,null=True,verbose_name=u'发布日期')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural=u'生活笔记'
        ordering = ['title']

class Actor(models.Model):
    '''
    演员集
    '''
    M = 'M'
    F = 'F'
    Sex_Choice = (
        (M,u'男'),(F,u'女'),
    )
    name = models.CharField(max_length=50,verbose_name=u'演员姓名')
    genter = models.CharField(max_length=2,choices=Sex_Choice,verbose_name=u'性别')
    birthday = models.DateField(blank=True,null=True,verbose_name=u'生日')
    tall = models.IntegerField(verbose_name=u'身高cm')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural=u'演员'
        ordering=['name']

class Director(models.Model):
    '''
    导演
    '''
    M = 'M'
    F = 'F'
    Sex_Choice = (
        (M,u'男'),(F,u'女'),
    )
    name = models.CharField(max_length=50,verbose_name=u'导演姓名')
    genter = models.CharField(max_length=30,choices=Sex_Choice,verbose_name=u'性别')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural=u'导演'
        ordering=['name']

class Movie(models.Model):
    '''
    电影
    导航栏中展示
    '''
    name = models.CharField(max_length=50,verbose_name=u'电影名称')
    movie_img = models.ImageField(upload_to='photos/movies',verbose_name=u'海报')    #添加电影海报 img 字段
    actor = models.ManyToManyField(Actor,verbose_name=u'演员')
    derector = models.ForeignKey(Director,verbose_name=u'导演')
    movie_intro = models.TextField(verbose_name=u'电影剧情')       #添加电影介绍
    movie_length = models.IntegerField(verbose_name=u'时长(分钟)')
    show_time = models.DateTimeField(verbose_name=u'上映时间')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural=u'电影'
        ordering = ['name']

class Program(models.Model):
    '''
    编程语
    '''
    pro_name = models.CharField(max_length=50,verbose_name=u'语言')
    creater = models.CharField(max_length=50,verbose_name=u'创始人')
    create_date = models.DateTimeField(blank=True,null=True,verbose_name=u'创始时间')
    pro_intro = models.TextField(verbose_name=u'语言介绍')

    def __str__(self):
        return self.pro_name
    class Meta:
        verbose_name_plural=u'编程语言'
        ordering = ['pro_name']

class Program_note(models.Model):
    '''
    编程笔记(教程)
    导航栏中展示
    '''
    pro_type = models.OneToOneField(Program,verbose_name=u'笔记类型')
    pro_title = models.CharField(max_length=100,verbose_name=u'标题')
    content = models.TextField(verbose_name=u'内容')
    pro_pub_date = models.DateTimeField(blank=True,null=True,verbose_name=u'发布日期')

    def __str__(self):
        return self.pro_title

    class Meta:
        verbose_name_plural=u'编程笔记'
        ordering = ['pro_title']


