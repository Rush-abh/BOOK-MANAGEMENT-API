"""
Program to configure API URLs of Author Details
Edited By: Rushabh Pancholi
"""

from django.urls import path
from authors import views


urlpatterns = [
    path('', views.authors_list),
    path('author/<int:author_id>', views.author_detail_view),
]
