"""
Program to test Author Details
Edited By: Rushabh Pancholi
"""

from django.test import TestCase
from authors.models import Author
from rest_framework.test import APITestCase


# testing model string
class TestModelsString(TestCase):
    def test_model_str(self):
        name = Author.objects.create(first_name="John", last_name="Watson")
        self.assertEqual(str(name), "John Watson")


# testing model fields
class TestModels(TestCase):
    def test_author_model(self):
        author = Author.objects.create(
            first_name="0knRNq7rOXEoXDx9sLx9az7sWDgnUfnnAiwG7Kco1KxDpq0s7ahC",
            last_name="sTvRu1BEajYBb6x4kiklUPyluKBzxBySpkT4D72rg3fLxWQufTO8",
        )


# testing POST request
class TestCreatingAuthorAPI(APITestCase):
    def test_author_created(self):
        data = {
            "first_name": "Eric",
            "last_name": " Prydz",
        }
        self.client.post("author/", data=data)
        #self.assertEqual(response, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)
