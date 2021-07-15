"""
Program to define model of Author Details
Edited By: Rushabh Pancholi
"""

from django.db import models

# author model


class Author(models.Model):
    author_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)

    def __str__(self):
        return "%s %s %s" % (self.author_id, self.first_name, self.last_name)
