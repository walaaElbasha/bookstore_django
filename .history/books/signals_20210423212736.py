from django.db.models.signals import post_save,pre_save,post_delete,pre_delete
from django.dispatch import receiver
from.models import Book,Isbn,User