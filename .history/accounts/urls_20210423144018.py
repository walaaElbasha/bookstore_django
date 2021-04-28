from django0urls import path
from . import views

urlpatterns =[
    path("",views.signup,name="signup" )

]  