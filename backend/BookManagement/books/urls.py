"""
Program to configure API URLs of Books Details
Edited By: Rushabh Pancholi
"""

from django.urls import path
from books import views


urlpatterns = [
    # display list
    path('', views.books_list),

    # update existing record
    path('book/<int:pk>', views.book_detail_view),

    # create new record
    path('book/', views.create_book),
]
