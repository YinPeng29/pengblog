#-*-coding:utf-8-*-
from django.contrib import admin

# Register your models here.
from .models import Publisher,Actor,Author,Program,Program_note,\
    Movie,Book,Director,Life_note


admin.site.register(Publisher)
admin.site.register(Actor)
admin.site.register(Author)
admin.site.register(Program)
admin.site.register(Program_note)
admin.site.register(Movie)
admin.site.register(Book)
admin.site.register(Director)
admin.site.register(Life_note)