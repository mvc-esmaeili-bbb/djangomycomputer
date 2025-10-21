from django.urls import path
from myapp1.views import products_view
from myapp1.views import ListView1

app_name = "myapp1"

urlpatterns = [
    path("fb/", products_view, name="fb"),
    path("cb/", ListView1.as_view(), name="cb"),
   
]
