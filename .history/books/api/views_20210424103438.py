#from django 
from rest_framework.response import Response
from rest_framework import status

def index(request):
    books = Book.object.objects.all()
    return Response