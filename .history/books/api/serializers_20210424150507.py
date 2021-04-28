from rest_framework import serializers
from books.models import Book, Isbn



class IsbnSerializer(serializers.ModelSerializer):
    class Meta:
        model=Isbn
        fields="__all__"
    class Meta:
       model=Book
       fields=(["tag"])
    

# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Book
#         fields=(["tag"])