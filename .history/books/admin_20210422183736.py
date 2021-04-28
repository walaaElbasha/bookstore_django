from django.contrib import admin
from .models import Book ,Category ,Isbn ,Tag
from django import forms 
from .forms import BookForm
from django.core.exceptions import ValidationError


class BookAdmin(admin.ModelAdmin):
    form=BookForm
    list_display=("title","author")
    list_filter=("categories",)

class BookInLine(admin.StackedInline):
    model=Book
    max_num =3
    extra =  1  
class TagAdmin(admin.ModelAdmin):
    inlines=[BookInLine]


class IsbnAdmin(admin.ModelAdmin):
    form=IsbnForm
    inlines=[BookInLine]


admin.site.register(Book,BookAdmin)
#admin.site.register(Book,BookForm)
#admin.site.register(BookInLine)
admin.site.register(Category)

admin.site.register(Tag,TagAdmin)
admin.site.register(Isbn,IsbnAdmin)
# admin.site.register(Tag,TagAdmin)