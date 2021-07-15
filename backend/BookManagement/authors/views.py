"""
Program to process the data of Author Details
Edited By: Rushabh Pancholi
"""
from rest_framework.response import Response
from rest_framework.decorators import api_view
from authors.models import Author
from .serializers import AuthorSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser


# function based view implementation
# Handles GET and POST request
@api_view(['GET', 'POST'])
def authors_list(request):

    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
