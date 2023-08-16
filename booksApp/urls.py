from django.urls import path
from .views import home, book_list

urlpatterns = [
    path('', home, name='home'),  # Root URL for the app
    path('books/', book_list, name='book_list'),
]

