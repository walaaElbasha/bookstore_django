from fjango.urls import path
from . import views


urlpatterns=[
    path("books",views.index),
    path("books",views.create),
    ]