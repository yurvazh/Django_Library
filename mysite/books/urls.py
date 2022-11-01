from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.show_books, name='book_info'),
    path('author/create', views.AuthorCreateView.as_view()),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name="author_info"),
    path('author/<int:pk>/update', views.AuthorUpdateView.as_view(), name="author_update_info"),
    path('create', views.BookCreateView.as_view()),
    path('<int:pk>/update', views.BookUpdateView.as_view())
]