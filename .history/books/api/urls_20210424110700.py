from fjango.urls import path
from . import views


urlpatterns=[
    path("books",views.create),
    path("books",views.index),
    ]