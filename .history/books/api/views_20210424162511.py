from django .shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from books.models import Book,Isbn
from .serializers import IsbnSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated,BasePermission
#from django.contrib.auth.decorators import api_view , permission_classes
#from rest_framework import 



# class IsViewer(BasePermission):
#     def has_permission(self,request,view):
#         return request.user.groups.filter(name="viewers").exists()



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
def destroy(request, pk):
    try: 
        isbn=Isbn.objects.get(pk=pk)
        isbn.delete()
        return Response(data={
        "success":True,
        "message":"Book has been deleted successfully",
        },
        status=status.HTTP_200_OK,
        )
    except Isbn.DoesNotExist: 
        return JsonResponse({'message': 'The book does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 

# @api_view(["GET"])
# @permission_classes[IsAuthenticated]
# def index(request):
#         books=


        