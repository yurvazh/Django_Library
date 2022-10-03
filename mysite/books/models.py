from django.db import models

# Create your models here.

class Author(models.Model):
    author_fullname = models.CharField(max_length=200)
    author_birthdate = models.DateTimeField('birth date')
    def __str__(self):
        return self.author_fullname


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.book_name
