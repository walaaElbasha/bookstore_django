from django .shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from books.models import Book,Isbn
from .serializers import IsbnSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated,BasePermission
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
#from django.contrib.auth.decorators import api_view , permission_classes
#from rest_framework import 



# class IsViewer(BasePermission):
#     def has_permission(self,request,view):
#         return request.user.groups.filter(name="viewers").exists()

@api_view(["POST"])
def api_signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
            "success": True,

            "message": "User has been registered successfully"

        }, status=status.HTTP_201_CREATED)
    return Response(data={

        "success": False,

        "errors": serializer.errors

    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])        
def index(request):
   #books = Book.objects.all()
   #serializer=BookSerializer(instance=books,many=True) 
    isbns=Isbn.objects.all()
    serializer=IsbnSerializer(instance=isbns,many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(["POST"])
def create(request):
    serializer=IsbnSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data={
        "success":True,
        "message":"Book has been created successfully",
        },
        status=status.HTTP_200_OK,
        )

    return Response(data={
        "success":False,
        "errors":serializer.errors
    },status=status.HTTP_404_BADREQUEST,
    
    )

@api_view(["DELETE"])
def destroy(request, id):
    try: 
        isbn=Isbn.objects.get(pk=id)
        isbn.delete()
        return Response(data={
        "success":True,
        "message":"Book has been deleted successfully",
        },
        status=status.HTTP_200_OK,
        )
    except Isbn.DoesNotExist: 
        return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND) 


@api_view(["PUT"])
def update(request, id):
        isbn=Isbn.objects.get(pk=id)
        isbn_data = JSONParser().parse(request) 
        isbn_serializer = IsbnSerializer(isbn, data=isbn_data) 
        if isbn_serializer.is_valid(): 
            isbn_serializer.save() 
            return JsonResponse(isbn_serializer.data) 
        return JsonResponse(isbn_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 


        