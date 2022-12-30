from django.shortcuts import render
from .serializers import  BookSerializer
from books.models import Book
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def BookAPI(request):
    #get all books
    #serialize them
    #return response
    if request.method=='GET':
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer=BookSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def Book_Detail(request,id):
    try:
        book=Book.objects.get(pk=id)
    except Book.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=BookSerializer(book)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method=='DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)