from django.urls import path
from .views import BookAPI,Book_Detail

urlpatterns = [
path("api/", BookAPI, name="book_list"),
path('api/<int:id>',Book_Detail,name='book-detial')
]