"""
Program to register book model Admin
Edited By: Rushabh Pancholi
"""
from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)
