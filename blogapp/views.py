from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render_to_response,get_object_or_404

# Create your views here.
from .models import Book,Life_note,Movie,Program_note

def Home(request):
    return render_to_response('home.html')

def Index(request):
    book_list = Book.objects.all()[0:3]
    life_note_list = Life_note.objects.all()[0:1]
    movie_list = Movie.objects.all()[0:2]
    program_note = Program_note.objects.all()[0:2]

    return render_to_response('index.html', {'book_list':book_list, 'life_note_list':life_note_list,
                                           'movie_list':movie_list,'program_note':program_note,}
                              )


def Book_list(request):
    book_list = Book.objects.all()
    counts = book_list.count()   #显示书籍条数
    return render_to_response('book_lists.html',{'book_list':book_list,'counts':counts})

def Book_detail(request,book_id):
    book_detail = get_object_or_404(Book,pk=book_id)
    return render_to_response('book_detail.html',{'book_detail':book_detail})

def Book_download(request):
    return ''
def Note_list(request):
    return ''
def Note_detail(reuest):
    return ''
def Movie_list(request):
    return ''
def Pronote_list(request):
    return ''
def Pronote_detail(request):
    return ''
def Pronote_share(request):
    return ''
def Login(request):
    return ""
def Register(request):
    return ''
def Logout(request):
    return ''
def Search(request):
    return ""
