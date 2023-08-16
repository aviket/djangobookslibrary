from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'booksApp/book_list.html', {'books': books})

def home(request):
    return render(request, 'booksApp/home.html')
