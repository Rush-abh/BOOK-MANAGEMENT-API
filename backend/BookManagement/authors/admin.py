"""
Program to register aurthors model Admin
Edited By: Rushabh Pancholi
"""
from django.contrib import admin
from .models import Author

# Register your models here.
admin.site.register(Author)
