"""
Program to serialize of Author Details
Edited By: Rushabh Pancholi
"""

from rest_framework import serializers
from authors.models import Author


# Default serializer with all field of model
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
