from django.urls import path
from . import views
from rest_fram

urlpatterns=[
    path("login",obtain_auth_token),
    path("",views.index),
    path("create",views.create),

    ]