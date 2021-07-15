"""
Program to serialize of Books Details
Edited By: Rushabh Pancholi
"""

from rest_framework import serializers
from books.models import Book


# Default serializer with all fields of model
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
