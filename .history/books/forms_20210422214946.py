from django import forms 
from .models import Book, Isbn,Category
from django.core.exceptions import ValidationError


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields="__all__"



class IsbnForm(forms.ModelForm):
     class Meta:
        model = Isbn
        fields='__all__'
        exclude=("isbn",)

     def clean_book_title(self):

        title=self.cleaned_data.get("book_title")
        titleLength=len(title)
        
        if titleLength<10:
            raise ValidationError("title should be more than 10 chars!")
        if titleLength>50:
            raise ValidationError("title should be less than 20 chars!")
        return title


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields='__all__'   
   
    def clean_category(self):
        category=self.cleaned_data.get("name")
        catLength=len(category)
        if catLength<2:
            raise ValidationError("category name length should be more than 2 chars!")