#from django 
from rest_framework.response import Response
from rest_framework import status
from books.models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view

def index(request):
    books = Book.object.objects.all()
    serializer=BookSerializer(instance=books,many=True)
    return Response(data=serializer.data,status=status_HTTP_200_ok)

@api_view(["POST"])
def create(request):
    serializer=BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        reutrn Response(data=serializer{
        "message":"Book has been created successfully"
        
        
        })
