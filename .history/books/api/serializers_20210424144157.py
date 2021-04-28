from rest_framework import serializers
from books.models import Book
from books.model import Isbn

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=("tag","isbn.bookAuthur","isbn.bookTitle")