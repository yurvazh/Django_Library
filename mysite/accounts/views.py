from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.template import loader
from django.views.generic import CreateView, ListView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/auth/login/'
    template_name = "accounts/signup.html"

def index(request):
    return HttpResponse("LOL")

class UsersView(ListView):
    model = User
    template_name = "accounts/index_users.html"
