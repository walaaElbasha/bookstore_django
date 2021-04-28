from django import forms 
from .models import Book
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields="__all__"

    def clean_title(self):
        title=self.cleaned_data.get("title")
        titleLength=len(title)
        #msh 3yza submit form f 7alt eno l2a elklma de
        if titleLength<10:
            raise ValidationError("title should be more than 10 chars!")
        if titleLength>20:
            raise ValidationError("title should be less than 20 chars!")
        return title

    def clean_category(self):
        category=self.cleaned_data.get("category")
        catLength=len(category)
        if catLength<2:
            raise ValidationError("category name length should be more than 2 chars!")
        return category


        