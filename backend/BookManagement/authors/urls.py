"""
Program to configure API URLs of Author Details
Edited By: Rushabh Pancholi
"""

from django.urls import path
from authors import views


urlpatterns = [
    # display list
    path('', views.authors_list),

    # update existing record
    path('author/<int:pk>', views.author_detail_view),

    # create new record
    path('author/', views.create_author),
]
