"""
Program to test Books Details
Edited By: Rushabh Pancholi
"""

from django.test import TestCase
from books.models import Book
from rest_framework.test import APITestCase


# testing model string
class TestModelsString(TestCase):
    def test_model_str(self):
        book = Book.objects.create(
            name="TestBook1", isbn="39283928", author="Testauthor1")
        self.assertEqual(str(book), "TestBook1 39283928 Testauthor1")


# testing model fields
class TestModels(TestCase):
    def test_author_model(self):
        book = Book.objects.create(
            name="JWwEDmJFP7u5o078j3dfTvStgduOqF31T0MmjnKljeQJ972PydtfHTEcgqT3LFiz9vdi71ONcHXXQixP16fj7HKxpW6lJHAItagFHfenPTh6tqN7boo1bVuie7WDW9TnSyuBvaIfzqvCOr5m97BF0UtyczSeyPQsBkYvQ6Fxg6KUVR4ov00Z27MfQRzPYyhmtj6qIoi9NtWT1cZxdUv8LpjbiybE7HKio6eHDjJjW8WDPTRmmCDcVzshmB",
            isbn="0428619512611",
            author="2"
        )


# testing POST request
class TestCreatingAuthorAPI(APITestCase):
    def test_author_created(self):
        data = {
            "name": "Eric",
            "isbn": " Prydz",
            "author": 3,
        }
        self.client.post("book/", data=data)
        #self.assertEqual(response, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
