
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("create",views.create,name='create'),
    path("edit/<str:isbn>",views.update,name="update"),
    path('edit/<str:isbn>', views.edit,name="edit"),  
    path('delete/<str:isbn>', views.destroy,name="delete"),  
      path('update/<str:isbn>', views.update,name="delete"), 
]
