from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author
from django.template import loader
from django.views.generic import DetailView, ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import Permission, User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token, csrf_protect

# Create your views here.
#def index(request):
    #books_list = Book.objects.all()
    
    #output = ''
    #for q in books_list:
      #  output = output + str(q.book_name + ' ' + q.book_author.author_fullname + '\n')
    #answer = "<html><body> %s \n %s \n %s \n %s \n</body></html>" % output
    #output = ','.join([(str(q.book_name) + ' ' +  str(q.book_author)) for q in books_list])
    #return HttpResponse(output)

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'books/author_details.html'

class AuthorCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "books.add_author"
    model = Author
    fields = ["author_fullname", "author_birthdate"]

class AuthorUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "books.change_author"
    model = Author
    fields = ["author_fullname", "author_birthdate"]

class BookCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "books.add_book"
    model = Book
    fields = ["book_name", "pub_date", "book_author"]

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "books.change_book"
    model = Book
    fields = ["book_name", "pub_date", "book_author"]

class BookDeleteView(DeleteView):
    model = Book
    success_url = '/books'
    template_name = "books/books_confirm_delete.html"

class AuthorDeleteView(DeleteView):
    model = Author
    success_url = '/books'
    template_name = "books/author_confirm_delete.html"

def index(request):
    user = get_object_or_404(User, pk=2)
    print(user.get_all_permissions())
    books_list = Book.objects.all()
    template = loader.get_template('books/index.html')
    context = {
        'books_list': books_list,
    }
    return HttpResponse(template.render(context, request))


def show_books(request, book_id):
    #book_all = Book.objects.all()
    #num = -1
    #response = "error: no book with that name"
    #for b in book_all:
     #   num += 1
      #  if (b.book_name == book_name):
       #     response = "Book #" + str(num + 1) + ": " + str(b.book_name) + " by " + str(b.book_author.author_fullname)
    book = get_object_or_404(Book, pk=book_id)

    return render(request, 'books/book_details.html', {'book': book})
