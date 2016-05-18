#-*-coding:utf-8-*-
from django.contrib import admin
from django.conf.urls import url


urlpatterns = [
    url(r'^$','blogapp.views.Home',name='home'),
    url(r'^book/list/$','blogapp.views.Book_list',name='booklist'),
    url(r'^book/detail/$','blogapp.views.Book_detail',name='bookdetail'),
    url(r'^book/download/$','blogapp.views.Book_download',name='bookdownload'),
    url(r'^lifenote/list/$','blogapp.views.Note_list',name='notelist'),
    url(r'^lifenote/detail/$','blogapp.views.Note_detail',name='notedetail'),
    url(r'^movie/list','blogapp.views.Movie_list',name='movielist'),
    url(r'^pronote/list','blogapp.views.Pronote_list',name='pronotelist'),
    url(r'^pronote/detail','blogapp.views.Pronote_detail',name='pronotedetail'),
    url(r'^pronote/share','blogapp.views.Pronote_share',name='pronoteshare'),
    url(r'^login','blogapp.views.Login',name='login'),
    url(r'^register','blogapp.views.Register',name='register'),
    url(r'^logout','blogapp.views.Logout',name='logout'),
    url(r'^search','blogapp.views.Search',name='search'),
]