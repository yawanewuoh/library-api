from django.shortcuts import render
from .models import Book
# Create your views here.

def Homepage(request):
    books=Book.objects.all()
    templates='books/homepage.html'
    context={
      'books':books
    }
    return render(request,templates,context)

