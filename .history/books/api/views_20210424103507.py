#from django 
from rest_framework.response import Response
from rest_framework import status
from books.models import Book

def index(request):
    books = Book.object.objects.all()
    return Response