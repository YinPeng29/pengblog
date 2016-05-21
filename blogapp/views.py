from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render_to_response

# Create your views here.
from .models import Book,Life_note,Movie,Program_note
def Home(request):
    book_list = Book.objects.all()[0:3]
    life_note_list = Life_note.objects.all()[0:1]
    movie_list = Movie.objects.all()[0:2]
    program_note = Program_note.objects.all()[0:2]
    try:
        b = Book.objects.get(id=1)
        author_list = b.author.all()
    except:
        pass
    # print (book_list)
    return render_to_response('home.html',{'book_list':book_list,'life_note_list':life_note_list,
                                           'movie_list':movie_list,'program_note':program_note,
                                           'author_list':author_list})

