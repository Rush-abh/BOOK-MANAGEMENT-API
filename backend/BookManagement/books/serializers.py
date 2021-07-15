"""
Program to serialize of Books Details
Edited By: Rushabh Pancholi
"""

from re import A
from django.db.models.expressions import F
from rest_framework import serializers
from books.models import Book
from authors.models import Author
from authors.serializers import AuthorSerializer


# serializer with all fields of model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


# serializer using Nested relationships with Author,
class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Book
        fields = ['name', 'isbn', 'author']
