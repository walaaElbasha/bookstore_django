from rest_framework import serializers
from books.models import Book



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Isbn
        fields="__all__"

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Book
#         fields=(["tag"])