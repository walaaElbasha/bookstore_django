from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
import uuid
from uuid import uuid4


class Category(models.Model):
    class Meta:
        verbose_name_plural="categories"
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
# class Metric(models.Model):
#     visits = models.IntegerField(null=True,blank=True)
#     ratio = models.DecimalField(null=True,blank=True,max_digits=2,decimal_places=1)
#     def _str_(self):
#         return f"{self.visits} visits | ratio: {self.ratio}"
class Tag(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name

class Isbn(models.Model):
    title=models.CharField( max_length=250)
    author=models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name="books")
    book_isbn = models.UUIDField(default=uuid.uuid4,
     unique=True, 
     db_index=True,
     max_length=200, 
     editable=False)

    def __str__(self):
        return self.title


class Book(models.Model):
    categories=models.ManyToManyField(Category)
    # metrics=models.OneToOneField(Metric,on_delete=models.CASCADE,null=True,blank=True)
    isbn= models.UUIDField(Isbn,primary_key=True, default=uuid.uuid4, editable=False )
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


