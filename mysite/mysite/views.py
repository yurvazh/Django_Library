from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.generic import DetailView, ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import Permission, User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token, csrf_protect


# Create your views here.


# books_list = Book.objects.all()

# output = ''
# for q in books_list:
#  output = output + str(q.book_name + ' ' + q.book_author.author_fullname + '\n')
# answer = "<html><body> %s \n %s \n %s \n %s \n</body></html>" % output
# output = ','.join([(str(q.book_name) + ' ' +  str(q.book_author)) for q in books_list])
# return HttpResponse(output)

