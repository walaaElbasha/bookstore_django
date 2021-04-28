from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BookForm
from .models import Book
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required(["books.view_book"])

def index(request):
    
    books= Book.objects.all()
    print(books)
    
    return render(request,"books/index.html",
    {
        "books":books,
       

    })

def create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request,"books/create.html",{
        "form":form
    })

def edit(request, isbn):  
    book = Book.objects.get(pk=isbn)  
    return render(request,'edit.html', {'book':book})  
    
def update(request,isbn):
    book = Book.objects.get(pk=isbn)
    form = BookForm(request.POST or None,instance=book)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request,"books/edit.html",{
        "form":form,
        "book":book
    })


def destroy(request, isbn):  
    book= Book.objects.get(pk=isbn)  
    book.delete()  
    return redirect("index") 




