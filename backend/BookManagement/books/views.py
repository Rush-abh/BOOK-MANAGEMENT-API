"""
Program to process the data of Book Details
Edited By: Rushabh Pancholi
"""
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from books.models import Book
from .serializers import BookSerializer, BookDetailSerializer


# function based view implementation
# Handles GET request, responds with record list
@csrf_exempt
@api_view(['GET'])
def books_list(request):

    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


# Handles GET,PUT and DELETE request, responds with updating existing record
@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail_view(request, pk):

    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookDetailSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Handles POST request, responds with creating new record
@csrf_exempt
@api_view(['POST'])
def create_book(request):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
