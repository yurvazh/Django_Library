from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book, Author
from django.template import loader
# Create your views here.
#def index(request):
    #books_list = Book.objects.all()
    
    #output = ''
    #for q in books_list:
      #  output = output + str(q.book_name + ' ' + q.book_author.author_fullname + '\n')
    #answer = "<html><body> %s \n %s \n %s \n %s \n</body></html>" % output
    #output = ','.join([(str(q.book_name) + ' ' +  str(q.book_author)) for q in books_list])
    #return HttpResponse(output)

def index(request):
    books_list = Book.objects.all()
    template = loader.get_template('books/index.html')
    context = {
        'books_list': books_list,
    }
    return HttpResponse(template.render(context, request))

def show_books(request, book_name):
    book_all = Book.objects.all()
    num = -1
    response = "error: no book with that name"
    for b in book_all:
        num += 1
        if (b.book_name == book_name):
            response = "Book #" + str(num + 1) + ": " + str(b.book_name) + " by " + str(b.book_author.author_fullname)

    
    return HttpResponse(response)